import streamlit as st
from urllib.parse import urlparse
from crawler import crawl
from llm_processor import generate_module_structure
from vector_store import build_faiss_index
import json

st.title("Pulse - Module Extraction AI Agent")
st.markdown("Extracts modules and submodules from product documentation URLs")

input_urls = st.text_area("Enter documentation URLs (comma-separated):")

if st.button("Start Extraction"):
    urls = [url.strip() for url in input_urls.split(",") if url.strip()]
    all_content = []
    for url in urls:
        st.write(f"Crawling: {url}")
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        content = crawl(url, domain)
        all_content.extend(content)

    joined_text = " ".join(all_content)

    if joined_text:
        st.write("Building FAISS index and processing...")
        index, vectorizer = build_faiss_index(all_content)
        st.write("Generating module structure using Gemini...")
        output = generate_module_structure(joined_text)
        st.json(output)

        with open("output.json", "w") as f:
            json.dump(output, f, indent=4)
        st.success("Extraction complete. Output saved to output.json")
    else:
        st.error("No documentation content found. Please check the URL(s).")


