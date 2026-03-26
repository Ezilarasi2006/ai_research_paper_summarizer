# AI Research Paper Summarizer

##  Overview

The AI Research Paper Summarizer is a web-based application that helps users quickly understand research papers by extracting key insights from PDF documents. It combines Natural Language Processing (NLP), data visualization, and interactive features to improve research efficiency.

##  Problem Statement

Research papers are often lengthy, complex, and time-consuming to read. Users struggle to quickly extract key information and insights. There is a need for an intelligent system that can automatically summarize research papers and provide meaningful insights in a short time.

##  Objective

* Extract text from research papers (PDF format)
* Generate concise summaries using AI
* Enable users to ask questions from the paper
* Provide insights like keywords and word frequency
* Support multiple languages for better accessibility

##  Features

###  Core Functionalities

* Upload research papers in PDF format
* Automatic text extraction
* AI-based summary generation
* Automatic paper title extraction

###  Interactive Features

* Ask questions from the paper
* Keyword-based answer retrieval
* Highlight important sentences and keywords

### Data Insights

* Word frequency analysis
* Keyword extraction
* Word cloud visualization
* Total words and sentence count

###  Language Support

* English
* Tamil
* Hindi
* Malayalam

###  User System

* User Registration & Login
* Password recovery
* Admin dashboard

##  Backend (FastAPI)

* Upload PDF files using API
* Extract text using PyMuPDF (fitz)
* Generate summaries
* Question-answering system
* UUID-based paper ID generation
* High-performance API handling

##  Frontend (Streamlit)

* Upload and preview PDFs
* Display title and summary
* Show insights and analytics
* Charts and visualizations
* Word cloud generation
* Multi-language support
* Highlight important content
* Interactive chat interface

##  Technologies Used

* Python
* FastAPI
* Streamlit
* PyMuPDF (fitz)
* PyPDF2
* SQLite
* Pandas
* Matplotlib
* WordCloud
* Google Translator API

**Note:** A sample database (`users.db`) is included for testing purposes.

##  Project Structure

```
AI_Paper_Summarizer/
│── backend_api.py
│── app.py
│── users.db
│── requirements.txt
│── README.md
│── docs/
    ├── user_stories.md
    ├── requirements.md
    └── sprint_plan.md
```

##  How to Run

### 1. Clone Repository

```bash
git clone https://github.com/Ezilarasi2006/ai_research_paper_summarizer.git
cd ai_research_paper_summarizer
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Backend

```bash
py -m uvicorn backend_api:app --reload
```

### 4. Run Frontend

```bash
py -m streamlit run app.py
```

##  Future Scope

* Integration of advanced AI models (LLMs)
* Improved question-answering accuracy
* Support for multiple PDF uploads
* Cloud deployment (AWS / Render / Azure)
* Mobile-friendly UI

##  Author

Ezilarasi L

##  License

This project is licensed under the MIT License.

##  Conclusion

This project demonstrates how AI, NLP, and web technologies can simplify research paper understanding, reduce reading time, and improve productivity for students and researchers.
