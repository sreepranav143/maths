import streamlit as st
import PyPDF2
import re

st.set_page_config(page_title="📘 Word Problem Solver", layout="centered")
st.title("📘 Word Problem Solver from PDF")

uploaded_file = st.file_uploader("📤 Upload your PDF with word problems", type=["pdf"])

def solve_word_problem(text):
    """
    Simple pattern matching for common word problems.
    Extend this to use NLP for complex problems.
    """
    # Example: If you have 24 cookies and want to share them equally with 4 friends, how many cookies does each friend get?
    match = re.search(r'(\d+)\s+.*?\s+(\d+)\s+friends?', text, re.IGNORECASE)
    if match:
        total = int(match.group(1))
        people = int(match.group(2))
        return f"✅ Each friend gets {total // people} items. ({total} ÷ {people})"
    
    # Fallback: Try extracting simple math expressions
    match = re.findall(r'\d+', text)
    if len(match) >= 2:
        try:
            result = int(match[0]) // int(match[1])
            return f"✅ Result: {result} ({match[0]} ÷ {match[1]})"
        except:  # noqa: E722
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
            solution = solve_word_problem(line)
            st.success(solution)
    except Exception as e:
        st.error(f"❌ Error reading or parsing PDF: {e}")
