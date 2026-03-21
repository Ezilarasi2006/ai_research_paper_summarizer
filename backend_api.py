from fastapi import FastAPI, UploadFile, File
import fitz
import uuid

app = FastAPI()

papers = {}

# -------------------------
# EXTRACT TEXT
# -------------------------
def extract_text(pdf_path):

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text("text")   # important

    return text


# -------------------------
# UPLOAD PDF
# -------------------------
@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    paper_id = str(uuid.uuid4())

    path = f"{paper_id}.pdf"

    with open(path, "wb") as f:
        f.write(await file.read())

    text = extract_text(path)

    print("TEXT LENGTH:", len(text))  # debug

    papers[paper_id] = text

    return {"paper_id": paper_id}


# -------------------------
# SUMMARIZE
# -------------------------
@app.post("/summarize")
def summarize(paper_id: str):

    text = papers.get(paper_id, "")

    if not text.strip():
        return {"summary": "No text extracted from PDF"}

    text = text.replace("\n", " ")

    sentences = text.split(".")

    sentences = [s.strip() for s in sentences if len(s) > 40]

    if not sentences:
        return {"summary": "Not enough content to summarize"}

    summary = ". ".join(sentences[:5])

    return {"summary": summary}


# -------------------------
# ASK (CHAT)
# -------------------------
@app.post("/ask")
@app.post("/ask")
def ask(paper_id: str, question: str):

    text = papers.get(paper_id, "")

    if not text.strip():
        return {"answer": "No paper found"}

    question = question.lower()

    clean_text = text.replace("\n", " ")

    sentences = clean_text.split(".")

    # -------------------------
    # TITLE FIX (IMPORTANT)
    # -------------------------
    if "title" in question:

        words = text.split()

        # Take first 12–15 words as title
        title = " ".join(words[:15])

        return {"answer": title}

    # -------------------------
    # DIRECT MATCH
    # -------------------------
    for s in sentences:
        if question in s.lower():
            return {"answer": s.strip()}

    # -------------------------
    # KEYWORD MATCH
    # -------------------------
    for word in question.split():
        for s in sentences:
            if word in s.lower():
                return {"answer": s.strip()}

    return {"answer": "Answer not found in the paper"}