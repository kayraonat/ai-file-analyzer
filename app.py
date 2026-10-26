import streamlit as st
import PyPDF2
from openai import OpenAI

#Page Settings
st.set_page_config(page_title="AI File Analyzer", page_icon="📄")
st.title("📄 AI File Analyzer")
st.write("Upload a PDF file, and AI will categorize it and summarize its content.")

#Gemini API Connection (Paste your API key here)
client = OpenAI(
     api_key="YOUR_API_KEY_HERE",
     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def read_pdf(file):
     try:
          reader = PyPDF2.PdfReader(file)
          text = ""
          for page in reader.pages:
               text += page.extract_text()
          return text
     except Exception as e:
          return f"Error reading file: {e}"

def analyze_text_with_ai(text):
     text = text[:3000]
     try:
          response = client.chat.completions.create(
               model="gemini-3.5-flash-lite",
               messages=[
                    {"role": "system", "content": "You are a helpful assistant"},
                    {"role": "user", "content": f"Analyze this document. Give me the Category (e.g., Software, Finance, Education) and a 2-sentence Summary.\n\nText:\n{text}"}
               ]
          )
          return response.choices[0].message.content
     except Exception as e:
          return f"AI Error: {e}"

# File Upload Area
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
     with st.spinner("Reading PDF..."):
          extracted_text = read_pdf(uploaded_file)

     if "Error" not in extracted_text:
          st.success("PDF Successfully Read!")

     # Drop-down menu for those who want to view the text
          with st.expander("View Extracted Text"):
               st.write(extracted_text[:1500] + "...")

          with st.spinner("AI is analyzing..."):
               ai_result = analyze_text_with_ai(extracted_text)

          st.subheader("AI Analysis Result:")
          st.info(ai_result)
     else:
          st.error(extracted_text)