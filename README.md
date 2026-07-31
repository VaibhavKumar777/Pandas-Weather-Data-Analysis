# Weather Data Analysis

## Description

A command-line Weather Data Analysis application built with Python and Pandas that allows users to load weather datasets and perform comprehensive weather analysis. The application provides dataset inspection, data cleaning, descriptive statistics, weather statistics, time-based analysis, filtering, sorting, grouping, and datetime conversion through an interactive CLI.

---

## Features

- Load weather datasets from CSV files
- Inspect datasets
  - Number of rows and columns
  - Data types
  - Missing value summary
  - Rows containing missing values
- Clean datasets
  - Remove missing values
  - Fill missing values with custom values
  - Preserve active dataset
- Convert date columns to datetime format
- Generate descriptive statistics for numerical columns
- Compute weather statistics
  - Highest temperature
  - Lowest temperature
  - Average temperature
  - Total rainfall
  - Average humidity
- Analyze weather data over time
  - Monthly analysis
  - Yearly analysis
  - Mean
  - Sum
  - Maximum
- Filter data by column values
- Sort datasets
  - Ascending
  - Descending
- Group datasets by two columns
- Input validation and exception handling

---

## Technologies

- Python
- Pandas

---

## Concepts Practiced

- DataFrames and Series
- CSV File Handling
- Missing Value Handling
- Data Cleaning
- Descriptive Statistics
- DateTime Conversion
- Time-Based Grouping
- GroupBy Operations
- Aggregate Functions
- Sorting Data
- Filtering Data
- Boolean Indexing
- Data Validation
- Exception Handling
- Modular Programming
- CLI Application Development

---

## Project Structure

```text
Weather Data Analysis/
│
├── main.py
├── analysis.py
├── weather_data.csv
└── README.md
```

---

## How to Run

Clone the repository.

```bash
git clone https://github.com/VaibhavKumar777/Pandas-Weather-Data-Analysis
```

Navigate to the project folder.

```bash
cd Weather-Data-Analysis
```

Install the required library.

```bash
pip install pandas
```

Run the application.

```bash
python main.py
```

---

## Sample Dataset

```csv
Date,Location,MaxTemp,MinTemp,Humidity,Rainfall,WindSpeed,Condition
2025-01-01,Delhi,24,12,65,0,12,Sunny
2025-01-02,Delhi,23,11,70,2,10,Cloudy
2025-01-03,Mumbai,30,24,85,18,20,Rainy
2025-01-04,Mumbai,31,25,88,25,22,Rainy
2025-01-05,Bengaluru,27,18,72,5,15,Cloudy
2025-01-06,Bengaluru,28,19,68,0,14,Sunny
2025-01-07,Chennai,33,26,80,10,18,Rainy
2025-01-08,Chennai,34,27,78,0,16,Sunny
2025-01-09,Kolkata,29,21,82,12,19,Rainy
2025-01-10,Kolkata,30,22,76,3,17,Cloudy
```

---

## Future Improvements

- Export filtered and grouped datasets to CSV
- Support Excel and JSON datasets
- Add weather visualizations using Matplotlib
- Generate monthly weather reports
- Compare weather across multiple locations
- Add custom aggregation functions
- Interactive dashboard using Streamlit
- Support multiple filtering conditions

---

## Time Taken

Approximately **90 minutes**

---

## Author

**Vaibhav Kumar**