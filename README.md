# Sales Data Cleaning Script

## Overview
This Python script performs data cleaning and preprocessing on a sales dataset (`sales_data.csv`). The goal is to prepare the dataset for analysis or machine learning by handling missing values, standardizing text, fixing date formats, correcting data types, and removing duplicates.

---

## Steps Performed

### 1. Load Dataset
- Reads the CSV file `sales_data.csv` using `pandas`.
- Prints the original shape and columns of the dataset.

### 2. Handle Missing Values
- **Drop rows with all NaN values** to remove completely empty rows.
- **Numeric columns**: Fill missing values with the **median** of the column.
- **Categorical columns**: Fill missing values with `"Unknown"`.

### 3. Remove Duplicates
- Removes duplicate rows to avoid redundancy in analysis.

### 4. Standardize Text Values
- **PaymentMode**: Converted to lowercase and stripped of extra spaces.
- **Category, Sub-Category, State, City**: Converted to title case for uniformity.

### 5. Fix Date Formats
- Converts `Order Date` to `datetime` format.
- Invalid dates are coerced to `NaT`.

### 6. Rename Columns
- Column names are converted to **lowercase** and spaces are replaced with underscores (`_`) for consistency and ease of use.

### 7. Correct Data Types
- `amount` and `profit`: Converted to `float`.
- `quantity`: Converted to `int`.

### 8. Save Cleaned Dataset
- Saves the cleaned dataset as `sales_data_cleaned.csv`.
