import pandas as pd

def load_file(filename):
    try:
        file = pd.read_csv(filename)
        return file
    except FileNotFoundError:
        return None
    except pd.errors.EmptyDataError:
        return None

def inspector(dataset):
    pass