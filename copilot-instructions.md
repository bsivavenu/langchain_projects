## Purpose
This repository contains many small LangChain/Streamlit demos and utilities. These instructions give an AI coding agent focused, repo-specific guidance to be productive quickly.

## Big picture
- **Monorepo of small apps**: most top-level demos live under `langchain_projects/` (many `app.py` Streamlit apps) and smaller tools under named folders like `rag_krish_naik/`.
- **Data and notebooks**: heavy use of Jupyter notebooks for experiments. Expect data, CSVs, and small serialized models under project subfolders (example: [langchain_projects/automatic_ticket_classification_tool/modelsvm.pk1](langchain_projects/automatic_ticket_classification_tool/modelsvm.pk1)).

## Key entrypoints
- Streamlit apps: run with `streamlit run <path>` (example: [langchain_projects/app.py](langchain_projects/app.py#L1-L120)).
- Small scripts: many folders have `app.py` or `main.py` (example: [rag_krish_naik/main.py](rag_krish_naik/main.py#L1-L20)).

## Important patterns & conventions
- Single-file apps: many demos are one-file (`app.py`) expecting to be executed directly via Streamlit or Python.
- Environment: projects use `.env` and expect secrets/API keys to be loaded via `dotenv`. Look for `load_dotenv()` calls in apps. Note: some apps load `.env` from parent dir (e.g., `load_dotenv(dotenv_path=Path("..")/".env")`).
- LangChain imports: this codebase uses newer split packages — e.g. `from langchain_openai import OpenAIEmbeddings` (not `langchain.embeddings`) and `from langchain_community.vectorstores import FAISS` (see [langchain_projects/app.py](langchain_projects/app.py#L1-L120)). When adding imports or fixes, mirror these sources.
- Per-project deps: many subfolders include `requirements.txt` — prefer installing per-project deps rather than a single global install unless asked otherwise.
- Multi-file tools: larger tools like `automatic_ticket_classification_tool/` and `csv_data_analysis_agent/` separate logic into `utils.py` for agent/processing logic and `app.py` for Streamlit UI. Follow this pattern when modularizing.
- Streamlit multi-page apps: directory structure like `automatic_ticket_classification_tool/pages/` uses Streamlit's multi-page feature. Files in `pages/` become linked tabs/pages automatically.

## Typical developer workflows (discovered)
- Create/activate venv: `python -m venv .venv && source .venv/bin/activate`.
- Install deps: `pip install -r <project>/requirements.txt` for the subproject you're working on. Root `pyproject.toml` lists common packages but is not authoritative for each demo.
- Run a demo: `streamlit run langchain_projects/app.py` or `python langchain_projects/your_tool/app.py` depending on the folder.
- Debugging: apps expect env variables; if behavior differs locally, check `load_dotenv()` and `myData.csv` or other local CSVs used by the app.

## Integration points & external dependencies
- OpenAI/embedding providers: many examples call `OpenAIEmbeddings` — ensure API keys are provided in environment before running.
- Vector DBs: FAISS is used for similarity search in simpler demos; Pinecone used in more complex tools like `automatic_ticket_classification_tool/`. Code uses `FAISS.from_documents(...)` or `PineconeVectorStore.from_existing_index()`.
- Embeddings: newer tools use `HuggingFaceEmbeddings` (via `langchain_huggingface`) for local/free embeddings alongside OpenAI embeddings. Mix patterns based on project needs.
- Serialized models: some tools depend on pre-built model files (e.g., SVM model at [langchain_projects/automatic_ticket_classification_tool/modelsvm.pk1](langchain_projects/automatic_ticket_classification_tool/modelsvm.pk1)); treat those as binary assets (use `joblib` to load).
- Common agents: `create_pandas_dataframe_agent` (CSV analysis), QA chains with `load_qa_chain()`, and custom chains for task-specific workflows.

## What to change and how to test
- Small feature or bugfix: update the relevant `app.py` or module, run the app locally via `streamlit run` or `python`, and validate with a few example inputs (many apps print results to console).
- Adding dependencies: update the subproject `requirements.txt` in that folder; do not assume a global `requirements.txt` applies to every demo.

## Examples to cite when editing code
- Use the Streamlit input pattern in [langchain_projects/app.py](langchain_projects/app.py#L40-L120) for UI-driven demos.
- Use `CSVLoader` usage in the same file for CSV-based ingestion patterns.

## Constraints for AI edits
- Preserve single-file demo patterns where present — prefer minimal, localized edits.
- Do not add new global infrastructure (DB servers, CI) without explicit instruction — this repo is demo-focused.
- When suggesting dependency changes, add them to the specific demo's `requirements.txt` and mention the run command to validate.

If anything above is unclear or you'd like more examples extracted from a particular subfolder, tell me which folder and I will iterate.
