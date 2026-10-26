import PyPDF2
from openai import OpenAI

client = OpenAI(
     api_key="YOUR_API_KEY_HERE",
     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def read_pdf(file_path):
     try:
          with open(file_path, 'rb') as file:
               reader = PyPDF2.PdfReader(file)
               text = ""
               for page in reader.pages:
                   text += page.extract_text()
               return text
     except Exception as e:
          return f"Error reading file {e}"

def analyze_text_with_ai(text):

     text = text[:2000]

     try:
          response = client.chat.completions.create(
               model="gemini-3.5-flash-lite",
               messages=[
                    {"role": "system", "content": "You are helpfull assistant that analyzes documents. "},
                    {"role": "user", "content": f"Analyze the following text. Determine its main category (e.g., Software, Finance, Education, Other) and provide a 2-sentence summary.\n\nText:\n{text}"}
               ]
          )
          return response.choices[0].message.content
     except Exception as e:
          return f"AI Error: {e}"

pdf_path = "test.pdf" 
extracted_text = read_pdf(pdf_path)

print("--- PDF Successfully Read ---")
# print(extracted_text[:500]) # İstersen okunan metni görebilirsin

print("\n--- AI Analysis ---")
ai_result = analyze_text_with_ai(extracted_text)
print(ai_result)     