AI Research Paper Summarizer
📌 Overview

The AI Research Paper Summarizer is a web-based application that helps users quickly understand research papers by extracting key insights from PDF documents. It combines Natural Language Processing (NLP), data visualization, and interactive features to provide summaries, keywords, and question-answering capabilities.

🚀 Features
📄 Core Functionalities
Upload research papers in PDF format
Automatic text extraction from documents
AI-based summary generation
Extract paper title automatically

💬 Interactive Features
Ask questions related to the paper
Keyword-based answer retrieval
Highlight important sentences and keywords

📊 Data Insights
Word frequency analysis
Keyword extraction
Word cloud visualization
Total words and sentence count

🌐 Language Support
Translate output into:
English
Tamil
Hindi
Malayalam

🔐 User System
User Registration & Login
Password recovery
Admin dashboard to monitor users


⚙️ Backend (FastAPI)

The backend is built using FastAPI to handle API requests efficiently.

🔧 Features
Upload PDF files using API
Extract text using PyMuPDF (fitz)
Generate summaries using sentence filtering
Question-answering using keyword matching
Unique paper ID generation using UUID
Fast and scalable API performance

🎨 Frontend (Streamlit)

The frontend is developed using Streamlit for an interactive UI.

✨ Features
Upload and preview research papers
Display extracted title and summary
Show insights like word count and sentence count
Generate charts and visualizations
Word cloud generation
Multi-language translation
Highlight important content
Interactive chat interface

🛠️ Technologies Used
Category	Tools / Libraries
Language	Python
Frontend	Streamlit
Backend	FastAPI
PDF Processing	PyMuPDF (fitz), PyPDF2
Database	SQLite
NLP	Regex, Text Processing
Visualization	Matplotlib, WordCloud
Translation	Google Translator

📂 Project Structure
AI_Paper_Summarizer/
│── backend.py          # FastAPI backend
│── app.py              # Streamlit frontend
│── users.db            # Database
│── requirements.txt
│── README.md

▶️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/Ezilarasi2006/ai_research_paper_summarizer.git
cd ai_research_paper_summarizer
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run Backend (FastAPI)
 py -m uvicorn backend_api:app --reload
4️⃣ Run Frontend (Streamlit)
 py -m streamlit run app.py



🔮 Future Scope
Integrate advanced AI models (LLMs) for better summaries
Improve accuracy of question-answering
Support multiple file uploads
Deploy on cloud platforms (AWS / Render / Railway)
Mobile responsive UI

screenshots:
![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)

👩‍💻 Author
Ezilarasi L

Conclusion:
This project demonstrates the effective use of AI and web technologies to simplify research paper analysis. It provides a user-friendly platform to extract insights, visualize data, and interact with academic content efficiently.