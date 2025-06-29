import streamlit as st
import PyPDF2
import re
import requests

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

assistant_id = "685f868a1c3507bfd53e4669"  # Your assistant ID

st.markdown("Chat with your Hugging Face assistant below:")

# Let the user enter their Hugging Face API key
user_token = st.text_input("🔑 Enter your Hugging Face API key:", type="password")

if user_token:
    if "history" not in st.session_state:
        st.session_state.history = []

    user_input = st.text_input("You:", "")

    if st.button("Send") and user_input:
        url = "https://hf.space/embed/huggingchat/chat-ui/api/conversation"
        headers = {
            "Authorization": f"Bearer {user_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "assistant_id": assistant_id,
            "inputs": user_input,
            "history": [
                {"role": "user", "content": msg["user"]} if msg["user"] else {"role": "assistant", "content": msg["assistant"]}
                for msg in st.session_state.history
            ]
        }

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            data = response.json()
            assistant_reply = data.get("generated_text", "No response.")
            st.session_state.history.append({"user": user_input, "assistant": assistant_reply})
        else:
            st.error(f"Error: {response.status_code} - {response.text}")

    # Display chat history
    for msg in st.session_state.history:
        st.markdown(f"**You:** {msg['user']}")
        st.markdown(f"**Assistant:** {msg['assistant']}")
else:
    st.info("Please enter your Hugging Face API key to chat with the assistant.")
