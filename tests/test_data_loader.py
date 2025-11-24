from src.data_loader import load_news
import pandas as pd

def test_load_news():
    df = load_news("sample.csv")  # Create a dummy file for testing
    assert isinstance(df, pd.DataFrame)
