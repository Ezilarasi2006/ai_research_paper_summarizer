AI Research Paper Summarizer
📌 Overview

The AI Research Paper Summarizer is a web-based application that helps users quickly understand research papers by extracting key insights from PDF documents. It combines NLP, visualization, and interactive features.

🚀 Features

📄 Core Functionalities
Upload research papers in PDF format
Automatic text extraction
AI-based summary generation
Extract paper title automatically

💬 Interactive Features
Ask questions from the paper
Keyword-based answer retrieval
Highlight important sentences and keywords

📊 Data Insights
Word frequency analysis
Keyword extraction
Word cloud visualization
Total words and sentence count

🌐 Language Support
English
Tamil
Hindi
Malayalam

🔐 User System
User Registration & Login
Password recovery
Admin dashboard

⚙️ Backend (FastAPI)
Upload PDF files using API
Extract text using PyMuPDF (fitz)
Generate summaries
Question-answering system
UUID-based paper ID
Fast API performance

🎨 Frontend (Streamlit)
Upload and preview PDFs
Show title and summary
Display insights
Charts and visualizations
Word cloud generation
Multi-language support
Highlight important content
Chat interface

🛠️ Technologies Used
Python
Streamlit
FastAPI
PyMuPDF (fitz)
PyPDF2
SQLite
Pandas
Matplotlib
WordCloud
Google Translator

📂 Project Structure
AI_Paper_Summarizer/
│── backend_api.py
│── app.py
│── users.db
│── requirements.txt
│── README.md

▶️ How to Run
1. Clone Repository
git clone https://github.com/Ezilarasi2006/ai_research_paper_summarizer.git
cd ai_research_paper_summarizer
2. Install Dependencies
pip install -r requirements.txt
3. Run Backend
py -m uvicorn backend_api:app --reload
4. Run Frontend
py -m streamlit run app.py


🔮 Future Scope
Integrate advanced AI models (LLMs)
Improve Q&A accuracy
Support multiple PDFs
Deploy to cloud
Mobile-friendly UI

👩‍💻 Author
Ezilarasi L

⭐ Conclusion

This project demonstrates how AI and web technologies can simplify research paper understanding and improve productivity.
