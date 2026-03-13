import docx
from pdfminer.high_level import extract_text

def read_docx(path):

    doc = docx.Document(path)

    text = []

    for para in doc.paragraphs:
        text.append(para.text)

    return " ".join(text)


def read_pdf(path):

    text = extract_text(path)

    return text