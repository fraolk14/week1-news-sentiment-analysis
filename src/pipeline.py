from src.data_loader import NewsDataLoader
from src.cleaning import HeadlineCleaner

class NewsPipeline:
    def __init__(self, data_path):
        self.loader = NewsDataLoader(data_path)
        self.cleaner = HeadlineCleaner()

    def run(self):
        df = self.loader.load_news()
        df['clean_headline'] = df['headline'].apply(self.cleaner.clean)
        return df
