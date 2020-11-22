
import numpy as np
from langdetect import detect as langdetect
from .apps import AppConfig

def cosine_similarity(v1, v2):
    mag1 = np.linalg.norm(v1)
    mag2 = np.linalg.norm(v2)
    if (not mag1) or (not mag2):
        return 0
    return np.dot(v1, v2) / (mag1 * mag2)

def detect_lang(text):
    try:
        lang_detected = langdetect(text)
    except Exception:
        lang_detected = ''
    return lang_detected

def embed(input):
    return AppConfig.model(input)

def generate_embeddings(content, content_lang):
    embedded_sentence = AppConfig.laser.embed_sentences(content, lang=content_lang)
    return embedded_sentence

def get_semantic_similarity(
    query_vec,
    data,
    vectors,
    df):
    results = []
    for idx, d in enumerate(data):
        doc_vec = vectors[idx].ravel()
        similarity = cosine_similarity(query_vec, doc_vec)
        results.append((similarity, d[:1000], idx))

    similarDocsSorted = sorted(results, key=lambda x: x[0], reverse=True)

    similar_docs = []
    similar_docs_dict = {}

    for eachDoc in similarDocsSorted[:10]:
        similar_docs_dict['score'] = eachDoc[0][0].astype(float)
        similar_docs_dict['matched_text'] = eachDoc[1]
        similar_docs_dict['original_doc'] = df['filename'].iloc[eachDoc[2]]
        similar_docs.append(similar_docs_dict.copy())

    return similar_docs

