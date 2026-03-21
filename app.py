import streamlit as st
import sqlite3
from PyPDF2 import PdfReader
from collections import Counter
import pandas as pd
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from deep_translator import GoogleTranslator

st.set_page_config(page_title="AI Research Paper Summarizer", layout="wide")

# -------------------------
# STYLE
# -------------------------
st.markdown("""
<style>
.stButton>button {
    background-color:#1f4e79;
    color:white;
    border-radius:10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;color:#1f4e79;'>🤖 AI Research Paper Summarizer</h1>", unsafe_allow_html=True)

# -------------------------
# DATABASE
# -------------------------
@st.cache_resource
def get_connection():
    conn = sqlite3.connect("users.db", check_same_thread=False)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS users(
    username TEXT PRIMARY KEY,
    password TEXT
    )
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS login_logs(
    username TEXT
    )
    """)

    conn.execute("INSERT OR IGNORE INTO users VALUES (?,?)", ("admin","admin123"))
    conn.commit()
    return conn

conn = get_connection()
cursor = conn.cursor()

# -------------------------
# SESSION
# -------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# -------------------------
# TRANSLATION
# -------------------------
def translate_text(text, language):
    lang_map = {"English":"en","Tamil":"ta","Hindi":"hi","Malayalam":"ml"}
    if language == "English":
        return text
    try:
        return GoogleTranslator(source='auto', target=lang_map[language]).translate(text)
    except:
        return text

# -------------------------
# STOPWORDS
# -------------------------
stopwords = {"a","an","the","and","or","is","are","was","were","to","of","in","on","for","with","that","this","it","as","by","at","from","be"}

# -------------------------
# FUNCTIONS
# -------------------------
def extract_text(pdf):
    reader = PdfReader(pdf)
    text = ""
    for page in reader.pages:
        t = page.extract_text()
        if t:
            text += t + " "
    return text

def get_title(text):
    for line in text.split("\n"):
        if len(line.strip()) > 10:
            return line
    return "Title not found"

def generate_summary(text):
    text = re.sub(r'\b[A-Z]{4,}\b', '', text)
    text = re.sub(r'\S+@\S+', '', text)
    text = re.sub(r'-\s+', '', text)
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    sentences = re.split(r'(?<=[.!?])\s+', text)
    sentences = [s.strip() for s in sentences if len(s) > 50]

    if not sentences:
        return "No meaningful content found."

    selected = sentences[:25]
    return " ".join([s.capitalize() for s in selected])

def extract_keywords(text):
    words = re.findall(r"\b[a-zA-Z]{4,}\b", text.lower())
    words = [w for w in words if w not in stopwords]
    return Counter(words).most_common(10)

def word_frequency(text):
    words = re.findall(r"\b[a-zA-Z]{4,}\b", text.lower())
    words = [w for w in words if w not in stopwords]
    return pd.DataFrame(Counter(words).most_common(10), columns=["Word","Count"])

def show_wordcloud(text):
    wc = WordCloud(width=800, height=400, background_color="white").generate(text)
    fig, ax = plt.subplots()
    ax.imshow(wc)
    ax.axis("off")
    st.pyplot(fig)

def chat_answer(question,text):
    sentences = re.split(r"[.\n]", text)
    for s in sentences:
        if question.lower() in s.lower():
            return s
    if "title" in question.lower():
        return sentences[0]
    return "Answer not found"

# -------------------------
# ADMIN VIEW USERS (FIXED)
# -------------------------
def view_logged_users():
    st.subheader("👀 Users Accessing App")

    # only non-admin count
    cursor.execute("SELECT COUNT(DISTINCT username) FROM login_logs WHERE username != 'admin'")
    st.metric("Total Users", cursor.fetchone()[0])

    # only unique non-admin users
    cursor.execute("""
        SELECT DISTINCT username 
        FROM login_logs 
        WHERE username != 'admin'
    """)

    users = cursor.fetchall()

    for u in users:
        st.write("•", u[0])

# -------------------------
# AUTH
# -------------------------
def register():
    st.subheader("Register")
    user = st.text_input("Username").strip().lower()
    pwd = st.text_input("Password", type="password").strip()

    if st.button("Register"):
        cursor.execute("SELECT * FROM users WHERE username=?", (user,))
        if cursor.fetchone():
            st.error("User already exists")
        else:
            cursor.execute("INSERT INTO users VALUES (?,?)",(user,pwd))
            conn.commit()
            st.success("Registered successfully")

def login():
    st.subheader("Login")
    user = st.text_input("Username").strip().lower()
    pwd = st.text_input("Password", type="password").strip()

    if st.button("Login"):
        cursor.execute("SELECT * FROM users WHERE username=?",(user,))
        data = cursor.fetchone()

        if not data:
            st.error("User not found")
        elif data[1] != pwd:
            st.error("Wrong password")
        else:
            st.session_state.logged_in = True
            st.session_state.username = user

            # log login
            cursor.execute("INSERT INTO login_logs VALUES (?)", (user,))
            conn.commit()

            st.success("Login successful")

def forgot_password():
    st.subheader("Forgot Password")
    user = st.text_input("Enter Username").strip().lower()

    if st.button("Get Password"):
        cursor.execute("SELECT password FROM users WHERE username=?", (user,))
        data = cursor.fetchone()

        if data:
            st.success(f"Your password is: {data[0]}")
        else:
            st.error("User not found")

# -------------------------
# DASHBOARD
# -------------------------
def dashboard():

    st.sidebar.success("Logged in as " + st.session_state.username)

    language = st.selectbox("🌐 Select Language",
                           ["English","Tamil","Hindi","Malayalam"])

    if st.session_state.username == "admin":
        menu = st.sidebar.radio("Menu",
        ["Users Activity","Summarizer","Insights","Keywords","Frequency","Word Cloud","Highlight","Chat"])
    else:
        menu = st.sidebar.radio("Menu",
        ["Summarizer","Insights","Keywords","Frequency","Word Cloud","Highlight","Chat"])

    if menu == "Users Activity":
        view_logged_users()
        return

    uploaded = st.file_uploader("Upload Research Paper PDF", type="pdf")
    text = ""

    if uploaded:
        reader = PdfReader(uploaded)
        st.write("Total Pages:", len(reader.pages))
        text = extract_text(uploaded)

        if text.strip():
            st.subheader("Paper Title")
            st.write(translate_text(get_title(text), language))
    else:
        st.info("Upload a research paper")

    if menu == "Summarizer":
        if uploaded and st.button("Generate Summary"):
            summary = translate_text(generate_summary(text), language)
            st.text_area("Summary", summary, height=200)
            st.download_button("Download Summary", summary)

    elif menu == "Insights":
        if uploaded:
            st.metric("Total Words", len(text.split()))
            st.metric("Total Sentences", len(text.split(".")))

    elif menu == "Keywords":
        if uploaded:
            df = pd.DataFrame(extract_keywords(text), columns=["Keyword","Frequency"])
            st.table(df)
            st.bar_chart(df.set_index("Keyword"))

    elif menu == "Frequency":
        if uploaded:
            df = word_frequency(text)
            st.bar_chart(df.set_index("Word"))

    elif menu == "Word Cloud":
        if uploaded:
            show_wordcloud(text)

    elif menu == "Highlight":
        if uploaded:
            st.subheader("📌 Highlighted Content")

            show_keywords = st.checkbox("Highlight Keywords", True)
            show_sentences = st.checkbox("Highlight Important Sentences", True)

            text = re.sub(r"-\s+", "", text)
            text = re.sub(r"\n+", " ", text)

            sentences = re.split(r"(?<=[.!?])\s+", text)

            total = len(sentences)
            step = max(1, total // 15)
            important_indexes = set(range(0, total, step))

            words = re.findall(r"\b[a-zA-Z]{5,}\b", text.lower())
            words = [w for w in words if w not in stopwords]
            keywords = [w for w, _ in Counter(words).most_common(25)]

            output = ""
            used_keywords = set()

            for i, sentence in enumerate(sentences):
                display = sentence

                if show_sentences and i in important_indexes:
                    display = f"<mark style='background-color:lightblue'>{display}</mark>"

                if show_keywords:
                    for word in keywords:
                        if word in used_keywords:
                            continue

                        if re.search(rf"\b{re.escape(word)}\b", display, re.IGNORECASE):
                            display = re.sub(
                                rf"\b{re.escape(word)}\b",
                                r"<mark style='background-color:yellow'>\g<0></mark>",
                                display,
                                count=1,
                                flags=re.IGNORECASE
                            )
                            used_keywords.add(word)

                output += display + " "

            st.markdown(
                f"<div style='height:400px;overflow:auto'>{output}</div>",
                unsafe_allow_html=True
            )

    elif menu == "Chat":
        if uploaded:
            q = st.text_input("Ask question")
            if st.button("Get Answer"):
                answer = translate_text(chat_answer(q,text), language)
                st.success(answer)

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

# -------------------------
# MAIN
# -------------------------
st.sidebar.title("📌 Navigation")

page = st.sidebar.radio("Go to",["Login","Register","Forgot Password"])

if st.session_state.logged_in:
    dashboard()
else:
    if page == "Login":
        login()
    elif page == "Register":
        register()
    else:
        forgot_password()