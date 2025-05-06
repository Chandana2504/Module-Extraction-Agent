#  Module Extraction AI Agent

An AI-powered agent that extracts structured module and submodule data from Zluri’s Help Center using advanced semantic search and LLM capabilities. Built using **Google Gemini**, **LangChain**, and **FAISS**, this tool automates documentation analysis and converts unstructured help articles into a clean JSON hierarchy.

---

## 🚀 Features

- 🌐 Crawls Zluri Help Center website.
- 🧠 Uses FAISS + Gemini for semantic understanding and structured data extraction.
- 📊 Returns data in hierarchical JSON format (Modules → Description → Submodules).
- 🧱 Built with modular, extendable code using LangChain components.
- 🛠 Fully local and runs in VS Code.

---

## 🛠 Tech Stack

- **Python**
- **streamlit**
- **FAISS** – Semantic vector search
- **LangChain** – LLM orchestration
- **Google Gemini** – LLM reasoning
- **BeautifulSoup** – Web scraping
- **dotenv** – Manage API keys

---

## 📂 Project Structure

ai-agent/
│
├── app.py # Main script to run the agent
├── vector_store.py # Code to build and query FAISS vector store
├── crawler.py # crwaling the help center websites (help.zluri.com)
├── output.json # Final structured module/submodule data
├──llm_processor.py
└── README.md # Project documentation
|__requirements.txt #Necessary modules are installed.

yaml
Copy
Edit

---

## 🧪 How It Works

1. **Scraping**: Extracts relevant help content from Zluri Help Center.
2. **Chunking & Embedding**: Breaks down text and creates vector embeddings using FAISS.
3. **Querying with LLM**: Sends a user query (e.g., “Extract modules from this content”) to Google Gemini.
4. **Parsing Output**: Cleans and validates the structured response into a usable JSON format.

---

## 🔧 Setup Instructions

Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set your Gemini API Key
Create a .env file:

ini
Copy
Edit
GEMINI_API_KEY=your_google_gemini_api_key
Run the agent

bash
Copy
Edit
python main.py
Check output
The extracted module and submodule data will be saved to output.json.

📈 Sample Output
json
Copy
Edit
[
  {
    "module": "Application Management",
    "Description": "Discover, monitor, and manage all SaaS applications...",
    "Submodules": {
      "Visibility": "Comprehensive app tracking...",
      "Discovery": "Integration with SSO, financial systems...",
      ...
    }
  }
]
