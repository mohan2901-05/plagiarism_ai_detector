import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("../dataset/ai_training_data.csv")

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(df["text"])

y = df["label"]

model = RandomForestClassifier()

model.fit(X, y)


def detect_ai(text):

    text_vec = vectorizer.transform([text])

    probability = model.predict_proba(text_vec)[0][1]

    return round(probability * 100, 2)