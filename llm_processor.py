import google.generativeai as genai
import os
import json

genai.configure(api_key=os.getenv("AIzaSyDgxwdAQXiaTJj2wIZvgzxFiqUCznjT1z0"))

def generate_module_structure(text_data):
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
You are an AI assistant. Based only on the below documentation text, extract high-level modules and their submodules, along with detailed descriptions.

Text:
\"\"\"
{text_data}
\"\"\"

Return the result in this JSON format:

[
  {{
    "module": "Module Name",
    "Description": "Module Description",##
    "Submodules": {{
      "Submodule 1": "Description of submodule 1",
      "Submodule 2": "Description of submodule 2"
    }}
  }}
]
"""

    response = model.generate_content(prompt)
    try:
        return json.loads(response.text)
    except Exception as e:
        return {"error": "Failed to parse response", "raw_output": response.text} 

