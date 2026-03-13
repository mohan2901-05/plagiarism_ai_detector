import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATASET_PATH = "../dataset/reference_documents"


def load_documents():

    docs = []
    names = []

    for file in os.listdir(DATASET_PATH):

        with open(os.path.join(DATASET_PATH, file), "r", encoding="utf-8") as f:
            docs.append(f.read())
            names.append(file)

    return docs, names


def detect_plagiarism(input_text):

    documents, filenames = load_documents()

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(documents + [input_text])

    similarity_scores = cosine_similarity(
        tfidf_matrix[-1], tfidf_matrix[:-1])

    scores = similarity_scores.flatten()

    max_score = scores.max()

    matched_doc = filenames[scores.argmax()]

    return round(max_score * 100, 2), matched_doc