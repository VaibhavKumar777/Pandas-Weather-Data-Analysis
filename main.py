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

load = 