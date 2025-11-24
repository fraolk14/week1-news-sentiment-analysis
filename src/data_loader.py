import pandas as pd

class NewsDataLoader:
    def __init__(self, path):
        self.path = path

    def load_news(self):
        return pd.read_csv(self.path)
