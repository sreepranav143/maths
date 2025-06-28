📘 Word Problem Solver from PDF
A simple Streamlit app that reads a PDF file containing math word problems, extracts them using basic text parsing, and solves simple arithmetic word problems like division and sharing.

🚀 Features
📤 Upload PDF files with word problems

🔍 Extract text automatically from PDF

🤖 Solve basic word problems like:

"If you have 24 cookies and want to share them equally with 4 friends, how many cookies does each friend get?"

📊 Displays answers directly in the app

📁 Project Structure
bash
Copy
Edit
word_problem_solver/
├── app.py               # Streamlit app
├── requirements.txt     # Dependencies
└── README.md            # This file
🔧 Installation & Setup
1. Clone the project or download manually
bash
Copy
Edit
git clone https://github.com/yourusername/word-problem-solver.git
cd word-problem-solver
2. Create and activate a virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv .venv
.venv\Scripts\activate      # On Windows
# source .venv/bin/activate  # On Mac/Linux
3. Install required packages
bash
Copy
Edit
pip install -r requirements.txt
▶️ Running the App
bash
Copy
Edit
streamlit run app.py
Then open the URL shown in your terminal (usually: http://localhost:8501)

📥 Example Input
PDF Content:

vbnet
Copy
Edit
If you have 24 cookies and want to share them equally with 4 friends, how many cookies does each friend get?
Output in App:

vbnet
Copy
Edit
✅ Each friend gets 6 items. (24 ÷ 4)
🧠 How It Works
Extracts raw text using PyPDF2

Uses regex to detect patterns like:

total items

number of people

sharing logic

Solves using simple Python math (no advanced AI yet)

📌 Limitations
Only solves simple division-style word problems

No OCR (doesn’t work on scanned images)

NLP parsing is limited (regex-based only)

✅ Future Improvements
Use spaCy or GPT to handle more complex problems

Add support for addition, subtraction, multiplication

Save history or export results

📚 Requirements
Python 3.7+

Streamlit

PyPDF2

