import re

class HeadlineCleaner:
    def clean(self, text: str):
        if not isinstance(text, str):
            return ""
        text = text.lower().strip()
        text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
        return text
