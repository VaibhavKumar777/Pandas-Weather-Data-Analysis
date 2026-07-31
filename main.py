import analysis
import pandas as pd
import sys
filename = input("Please enter the dataset filename with extension(.csv): ")

dataset = analysis.load_file(filename)
active_dataset = None

if dataset is not None:
    active_dataset = dataset
else:
    print(f"Could not load the file {filename} it Doesn't exist or is Empty Please check again\n")
    sys.exit()
def inspecting(active_dataset):
    rows,cols,datatype,total_missing,missing_values = analysis.inspector(active_dataset)
    print(f"Number of Rows: {rows}\nNumber of Columns: {cols}\nData Types:\n{datatype}\nTotal Missing Values: {total_missing}\nMissing Values:\n{missing_values}\n")

def cleaner():
    global active_dataset
    print("Please select a cleaning option:\n1. Drop rows with missing values\n2. Fill missing values with a specific value\n3. Do nothing\n")
    choice = int(input())
    if choice == 1:
        active_dataset = analysis.data_cleaner(active_dataset,choice,None)
        print("Rows with missing values have been dropped.\n")
    elif choice == 2:
        what = input("Please enter the value to fill missing values with: ")
        active_dataset = analysis.data_cleaner(active_dataset,choice,what)
        print(f"Missing values have been filled with {what}.\n")
    elif choice == 3:
        print("No cleaning has been done.\n")
    else:
        print("Invalid choice. Please try again.\n")
def change_to_date():
    global active_dataset
    column = input("Please enter the column name to convert to datetime: ")
    changed_dataset = analysis.to_datetime(active_dataset,column)
    if changed_dataset is not None:
        print(f"Column {column} has been converted to datetime.\n")
        active_dataset = changed_dataset
    else:
        print(f"Column {column} does not exist in the dataset.\n")
def numerical_stats(active_dataset):
    stats = analysis.numerical_statistics(active_dataset)
    print(f"Numerical Statistics:\n{stats}\n")

def specific_stats(active_dataset):
    temp_column = input("Please enter the temperature column name: ")
    rainfall_columns = input("Please enter the rainfall column name (or leave blank if not applicable): ")
    humidity_column = input("Please enter the humidity column name (or leave blank if not applicable): ")
    rainfall_columns = rainfall_columns if rainfall_columns else None
    humidity_column = humidity_column if humidity_column else None
    stats = analysis.stats(active_dataset,temp_column,rainfall_columns,humidity_column)
    if stats is not None:
        highest_temp,lowest_temp,avg_temp,total_rainfall,avg_humidity = stats
        print(f"Highest Temperature: {highest_temp}\nLowest Temperature: {lowest_temp}\nAverage Temperature: {avg_temp}\nTotal Rainfall: {total_rainfall}\nAverage Humidity: {avg_humidity}\n")
    else:
        print(f"Temperature column {temp_column} does not exist in the dataset.\n")
def analyze_time(active_dataset):
    column = input("Please enter the column name to analyze over time: ")
    while True:
        try:
            what_to_calc = int(input("Please select what to calculate:\n1. Average\n2. Sum\n3. Max\n"))
            how = int(input("Please select how to group the data:\n1. Monthly\n2. Yearly\n"))
            break
        except ValueError:
            print("Invalid input. Please enter a number.\n")
    how = "monthly" if how == 1 else "yearly"
    result = analysis.analyze_overtime(active_dataset,column,what_to_calc,how)
    if result is not None:
        print(f"Result of analysis over time:\n{result}\n")
    else:
        print(f"Column {column} does not exist in the dataset.\n")
def filteration(active_dataset):
    column = input("Please enter the column name to filter: ")
    value = input("Please enter the value to filter by: ")
    filtered_data = analysis.filter_data(active_dataset,column,value)
    if filtered_data is not None:
        print(f"Filtered Data:\n{filtered_data}\n")
        return filtered_data
    else:
        print(f"Column {column} does not exist in the dataset.\n")
def sort_data(active_dataset):
    column = input("Please enter the column name to sort by: ")
    while True:
        ascending_input = input("Please enter 'True' for ascending order or 'False' for descending order: ")
        if ascending_input.lower() == 'true':
            ascending = True
            break
        elif ascending_input.lower() == 'false':
            ascending = False
            break
        else:
            print("Invalid input. Please enter 'True' or 'False'.\n")
    sorted_data = analysis.sort_weather(active_dataset,column,ascending)
    if sorted_data is not None:
        print(f"Sorted Data:\n{sorted_data}\n")
        return sorted_data
    else:
        print(f"Column {column} does not exist in the dataset.\n")
def group_data(active_dataset):
    col1 = input("Please enter the first column name to group by: ")
    col2 = input("Please enter the second column name to group by: ")
    grouped_data = analysis.group_data(active_dataset,col1,col2)
    if grouped_data is not None:
        print(f"Grouped Data:\n{grouped_data}\n")
        return grouped_data
    else:
        print(f"One or both columns {col1} and {col2} do not exist in the dataset.\n")
while True:
    print("Welcome to the Weather Data Analysis Program\n")
    try:
        user = int(input("Please select an option:\n1. Inspect the dataset\n2. Clean the dataset\n3. Convert a column to datetime\n4. Get numerical statistics\n5. Get specific statistics\n6. Analyze over time\n7. Filter Data\n8. Sort Data\n9. Group Data\n10. Exit\n"))
        if user == 1:
            inspecting(active_dataset)
        elif user == 2:
            cleaner()
        elif user == 3:
            change_to_date()
        elif user == 4:
            numerical_stats(active_dataset)
        elif user == 5:
            specific_stats(active_dataset)
        elif user == 6:
            analyze_time(active_dataset)
        elif user == 7:
            filtered_data = filteration(active_dataset)
        elif user == 8:
            sorted_data = sort_data(active_dataset)
        elif user == 9:
            grouped_data = group_data(active_dataset)
        elif user == 10:
            print("Exiting the program. Goodbye!\n")
            sys.exit()
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 10.\n")