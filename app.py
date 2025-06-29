import streamlit as st
import PyPDF2
import re

st.set_page_config(page_title="📘 Math problems", layout="centered")
st.title("📘 Math Problems ")

uploaded_file = st.file_uploader("📤 Upload your PDF with math problems", type=["pdf"])

def solve_math_problem(text):
    """
    Simple pattern matching for common math problems.
    Extend this to use NLP for complex problems.
    """
    match = re.search(r'(\d+)\s+.*?\s+(\d+)\s+friends?', text, re.IGNORECASE)
    if match:
        total = int(match.group(1))
        people = int(match.group(2))
        return f"✅ Each friend gets {total // people} items. ({total} ÷ {people})"
    
    match = re.findall(r'\d+', text)
    if len(match) >= 2:
        try:
            result = int(match[0]) // int(match[1])
            return f"✅ Result: {result} ({match[0]} ÷ {match[1]})"
        except:
            return "⚠️ Unable to divide safely."
    
    return "❌ Could not understand the problem."

if uploaded_file:
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        full_text = ""
        for page in pdf_reader.pages:
            full_text += page.extract_text()

        st.subheader("📄 Extracted Problems:")
        lines = full_text.strip().split("\n")
        for idx, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
            st.markdown(f"**Problem {idx + 1}:** {line}")
            solution = solve_math_problem(line)
            st.success(solution)
    except Exception as e:
        st.error(f"❌ Error reading or parsing PDF: {e}")

st.title("Math Problems Assistant")

st.markdown("Chat with your Hugging Face assistant below:")
st.markdown("**Please enter your Hugging Face API key below to chat with the assistant.**")

# Let the user enter their Hugging Face API key
user_token = st.text_input("🔑 Enter your Hugging Face API key:", type="password")

# Chat input and chat history are disabled as requested
if user_token:
    st.info("Chat input is currently disabled as requested.")
else:
    st.info("Please enter your Hugging Face API key to chat with the assistant.")
