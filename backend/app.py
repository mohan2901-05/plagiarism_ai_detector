from flask import Flask, request, jsonify
import os
from flask_cors import CORS

from plagiarism_engine import detect_plagiarism
from ai_detector import detect_ai
from file_parser import read_docx, read_pdf


app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "../uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/analyze", methods=["POST"])
def analyze():

    text = ""

    # If user uploads a file
    if "file" in request.files:

        file = request.files["file"]

        if file.filename != "":

            path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

            file.save(path)

            if file.filename.endswith(".docx"):
                text = read_docx(path)

            elif file.filename.endswith(".pdf"):
                text = read_pdf(path)

            else:
                with open(path, "r", encoding="utf-8") as f:
                    text = f.read()

    # If user enters text
    if text == "":
        text = request.form.get("text")

    plagiarism_score, source = detect_plagiarism(text)

    ai_probability = detect_ai(text)

    return jsonify({
        "plagiarism_score": plagiarism_score,
        "matched_source": source,
        "ai_probability": ai_probability
    })


if __name__ == "__main__":
    app.run(debug=True)