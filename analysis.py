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
    rows = dataset.shape[0]
    cols = dataset.shape[1]
    datatype = dataset.dtypes
    total_missing = dataset.isna().sum().sum()
    missing_values = dataset[dataset.isna().any(axis=1)]
    return rows,cols,datatype,total_missing,missing_values

def data_cleaner(dataset,choice,what):
    if choice == 1:
        return dataset.dropna()
    elif choice == 2:
        return dataset.fillna(what)
    elif choice == 3:
        return dataset

def column_validator(dataset,column):
    if column not in dataset.columns:
        return False
    return True

def to_datetime(dataset,column):
    if column_validator(dataset,column):
        dataset[column] = pd.to_datetime(dataset[column])
        return dataset
    return None

def numerical_statistics(dataset):
    return dataset.select_dtypes(include=['number']).describe()

def stats(dataset,temp_column,rainfall_columns=None,humidity_column=None):
    total_rainfall = None
    avg_humidity = None
    if column_validator(dataset,temp_column):
        highest_temp = dataset[temp_column].max()
        lowest_temp = dataset[temp_column].min()
        avg_temp = dataset[temp_column].mean()
    else:
        return None
    if rainfall_columns is not None:
        if column_validator(dataset,rainfall_columns):
            total_rainfall = dataset[rainfall_columns].sum()
    if humidity_column is not None:
        if column_validator(dataset,humidity_column):
            avg_humidity = dataset[humidity_column].mean()
    return highest_temp,lowest_temp,avg_temp,total_rainfall,avg_humidity

def helper(dataset, column, how):
    if how == "monthly":
        return dataset.groupby(dataset[column].dt.to_period("M"))
    elif how == "yearly":
        return dataset.groupby(dataset[column].dt.year)
    else:
        return None

def analyze_overtime(dataset,column,what_to_calc,how="monthly"):
    if not column_validator(dataset,column):
        return None
    grouped = helper(dataset,column,how)
    if grouped is None:
        return None
    if what_to_calc == 1:
        return grouped.mean()
    elif what_to_calc == 2:
        return grouped.sum()
    elif what_to_calc == 3:
        return grouped.max()
    else:
        return None

def filter_data(dataset,column,value):
    if column_validator(dataset,column):
        return dataset[dataset[column].astype(str).str.contains(value, case=False, na=False)]
    return None

def sort_weather(dataset,column,ascending=True):
    if column_validator(dataset,column):
        return dataset.sort_values(by=column,ascending=ascending)
    return None

def group_data(dataset,col1,col2):
    if column_validator(dataset,col1) and column_validator(dataset,col2):
        grouped = dataset.groupby([col1,col2])
        return grouped
    return None