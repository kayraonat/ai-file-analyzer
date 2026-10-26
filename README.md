# AI File Analyzer

An intelligent web application built with Python, Streamlit, and Google's Gemini AI. It allows users to upload a PDF document, automatically extracts the text, and uses AI to categorize the document and provide a concise summary.

## Features
- **PDF Text Extraction:** Reads and extracts text from uploaded PDF files using PyPDF2.
- **AI-Powered Analysis:** Connects to the Gemini API via the OpenAI Python library to analyze the text.
- **Automated Categorization:** Automatically identifies the document's category (e.g., Software, Finance, Education).
- **Smart Summarization:** Generates a 2-sentence summary of the document's core message.
- **Interactive UI:** A clean, user-friendly interface built with Streamlit.

## Technologies Used
- **Python 3**
- **Streamlit** (Web interface)
- **PyPDF2** (PDF parsing)
- **OpenAI Python Library** (Used for Gemini API integration)
- **Google Gemini AI** (gemini-2.5-flash model)

## What I Learned
Building this project helped me understand:
- How to handle file uploads and process PDFs in a web application.
- Integrating Large Language Models (LLMs) into Python scripts using APIs.
- Structuring a Streamlit application with states and error handling.
- Writing prompts to get structured, accurate responses from AI.

## How to Run Locally

1. Clone the repository:
   git clone https://github.com/kayraonat/ai-file-analyzer.git

2. Navigate to the folder and create a virtual environment:
   python -m venv venv

3. Activate the environment and install dependencies:
   pip install streamlit PyPDF2 openai

4. Replace "YOUR_API_KEY_HERE" in app.py with your own Gemini API key.

5. Run the app:
   streamlit run app.py

---
Created by [Kayra Onat](https://github.com/kayraonat)
