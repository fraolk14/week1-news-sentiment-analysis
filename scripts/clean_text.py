import re

def clean_headline(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text
