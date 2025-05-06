from sklearn.feature_extraction.text import TfidfVectorizer
import faiss
import numpy as np

def build_faiss_index(text_chunks):
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform(text_chunks).toarray().astype('float32')

    dim = vectors.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(vectors)

    return index, vectorizer
