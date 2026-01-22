import pdfplumber
import re

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            txt = page.extract_text()
            if txt:
                text += txt + "\n"
    return text



file_path = "../../Ancient_History_Previous_Year_Questions_UPSC.pdf"

pattern = re.compile(
    r"Q\d+\.([\s\S]*?)(?:\([a-dA-D]\)[\s\S]*?Correct answer:\s*([a-dA-D]))",
    re.MULTILINE
)

matches = re.findall(
    r"Q\d+\.\s*(.*?)\n\s*\(a\)\s*(.*?)\n\s*\(b\)\s*(.*?)\n\s*\(c\)\s*(.*?)\n\s*\(d\)\s*(.*?)\n\s*Correct answer:\s*([a-dA-D])",
    extract_text_from_pdf(file_path),
    re.DOTALL
)


questions = []
for q_text, opt_a, opt_b, opt_c, opt_d, correct in matches:
    questions.append({
        "question_text": q_text.strip(),
        "options": {"A": opt_a.strip(), "B": opt_b.strip(), "C": opt_c.strip(), "D": opt_d.strip()},
        "correct_answer": correct.upper(),
        "explanation": None,
        "source": file_path,
        "topic": "Polity PYQ",
        "difficulty": 3
    })


from supabase import create_client
import os
from dotenv import load_dotenv
load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
supabase = create_client(url, key)

# Batch insert for speed
supabase.table("quiz_questions").insert(questions).execute()


data = supabase.table("quiz_questions").select("*").limit(5).execute()
# print(data)



################
""" Display sample questions from Supabase """
# import random

# rows = supabase.table("quiz_questions").select("*").execute().data
# sample = random.sample(rows, 5)

# for idx, q in enumerate(sample, start=1):
#     print(f"\nQ{idx}. {q['question_text']}")
#     for k, v in q["options"].items():
#         print(f"  {k}. {v}")
#     print(f"✅ Correct Answer: {q['correct_answer']}")

################

