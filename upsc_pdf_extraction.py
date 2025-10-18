

import pdfplumber
import os
import time
import json
from dotenv import load_dotenv
load_dotenv()

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

pdf_text = extract_text_from_pdf("../../polity_prelims_questions_a5ffe5d551.pdf")


from langchain.text_splitter import CharacterTextSplitter

# safer defaults: smaller chunks to reduce token usage per request
splitter = CharacterTextSplitter(
    chunk_size=int(os.getenv("CHUNK_SIZE", "600")),  # number of characters per chunk
    chunk_overlap=int(os.getenv("CHUNK_OVERLAP", "50"))
)
chunks = splitter.split_text(pdf_text)


from openai import OpenAI
import tiktoken

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise EnvironmentError("OPENAI_API_KEY not set in environment")
client = OpenAI(api_key=openai_api_key)

# Configurable model and token limits
MODEL = os.getenv("OPENAI_MODEL", "gpt-4")
MAX_INPUT_TOKENS = int(os.getenv("MAX_INPUT_TOKENS", "8000"))
MAX_OUTPUT_TOKENS = int(os.getenv("MAX_OUTPUT_TOKENS", "800"))

enc = tiktoken.encoding_for_model(MODEL)

def estimate_tokens(text: str) -> int:
    if not text:
        return 0
    return len(enc.encode(text))


def generate_questions(chunk, max_retries=3):
    # Prompt asks for JSON so parsing is deterministic and output is smaller
    prompt = f"""
    Extract up to 5 multiple-choice questions from the following text as a JSON array.
    Each item should be an object with keys: question_text, options (dict of A-D), correct_answer (A-D), explanation.
    Example output:
    [{{"question_text":"...","options":{{"A":"...","B":"...","C":"...","D":"..."}},"correct_answer":"A","explanation":"..."}}]

    Text:
    {chunk}
    """

    # Estimate tokens and avoid sending too-large inputs
    input_tokens = estimate_tokens(prompt)
    if input_tokens > MAX_INPUT_TOKENS:
        # truncate chunk conservatively
        # reduce characters proportional to token excess
        ratio = MAX_INPUT_TOKENS / input_tokens
        truncate_len = int(len(chunk) * ratio * 0.95)
        chunk = chunk[:truncate_len]
        prompt = f"""
    Extract up to 5 multiple-choice questions from the following text as a JSON array.
    Each item should be an object with keys: question_text, options (dict of A-D), correct_answer (A-D), explanation.

    Text:
    {chunk}
    """

    attempt = 0
    backoff = 1
    while attempt <= max_retries:
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=MAX_OUTPUT_TOKENS
            )
            text = None
            # guard access: some SDK responses may vary
            if hasattr(response, 'choices') and len(response.choices) > 0:
                msg = response.choices[0].message
                if msg and hasattr(msg, 'content'):
                    text = msg.content
            if text is None:
                # fallback to str(response)
                text = str(response)
            # try to parse JSON; if it fails, return raw text for manual review
            try:
                parsed = json.loads(text)
                return parsed
            except Exception:
                # sometimes the model emits code fences or extra text
                # attempt to extract the first JSON block
                start = text.find("[") if isinstance(text, str) else -1
                end = text.rfind("]") if isinstance(text, str) else -1
                if start != -1 and end != -1:
                    try:
                        parsed = json.loads(text[start:end+1])
                        return parsed
                    except Exception:
                        return text
                return text

        except Exception as e:
            # handle rate limits and retry with exponential backoff
            err_str = str(e)
            if "RateLimitError" in err_str or "rate_limit" in err_str or getattr(e, 'status_code', None) == 429:
                attempt += 1
                time.sleep(backoff)
                backoff *= 2
                continue
            else:
                # other exceptions: re-raise
                raise


# Configurable processing limits
MAX_CHUNKS = int(os.getenv("MAX_CHUNKS", "0"))  # 0 means process all
RATE_SLEEP_SEC = float(os.getenv("RATE_SLEEP_SEC", "0.5"))

questions_list = []
to_process = chunks if MAX_CHUNKS == 0 else chunks[:MAX_CHUNKS]
for idx, chunk in enumerate(to_process, start=1):
    print(f"Processing chunk {idx}/{len(to_process)}")
    questions_text = generate_questions(chunk)
    questions_list.append(questions_text)
    time.sleep(RATE_SLEEP_SEC)



questions_db = []

def normalize_and_add(item, source="example.pdf"):
    # item may already be a dict with expected keys
    if not isinstance(item, dict):
        # fallback: store raw text as question_text
        questions_db.append({
            "question_text": str(item),
            "options": {},
            "correct_answer": None,
            "explanation": None,
            "source": source,
            "topic": "Chapter 1",
            "difficulty": 3
        })
        return

    q_text = item.get("question_text") or item.get("question") or item.get("q")
    options = item.get("options") or item.get("choices") or {}
    correct = item.get("correct_answer") or item.get("answer")
    explanation = item.get("explanation") or item.get("explain")

    questions_db.append({
        "question_text": q_text,
        "options": options,
        "correct_answer": correct,
        "explanation": explanation,
        "source": source,
        "topic": "Chapter 1",
        "difficulty": 3
    })


for q in questions_list:
    # q can be a list (parsed JSON array), a dict, or a string (parse failed)
    if isinstance(q, list):
        for item in q:
            normalize_and_add(item)
    else:
        # q is either a dict or a string
        normalize_and_add(q)


from supabase import create_client
from supabase import create_client


key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")   # Must be the service role key

url = "https://mohznqifkzoehgagwguq.supabase.co"

if not key:
    raise EnvironmentError("SUPABASE_API_KEY not set in environment")

supabase = create_client(url, key)

for q in questions_db:
    supabase.table("quiz_questions").insert(q).execute()


