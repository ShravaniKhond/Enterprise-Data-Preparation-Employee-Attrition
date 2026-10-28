
# Enterprise Data Preparation for Employee Attrition

## Project Overview
This project prepares the IBM HR Analytics Employee Attrition dataset for further analysis.

## Activities Performed
1. Imported the HR dataset using Pandas.
2. Checked and handled missing values.
3. Detected and removed duplicate records.
4. Detected potential numeric outliers using the IQR method.
5. Encoded categorical variables using one-hot encoding.

## Dataset Summary
- Original records: 1,470
- Original columns: 35
- Missing values found: 0
- Duplicate rows found: 0

## Tools Used
- Python
- Pandas
- VS Code

## Generated Outputs
- `employee_attrition_cleaned.csv`
- `employee_attrition_cleaned_encoded.csv`
- `outlier_summary.csv`
- `preparation_report.csv`

## Important Notes
- Outliers are detected and reported, not automatically removed.
- No missing values or duplicate rows were found in the original dataset.
- The encoded dataset is prepared for further analysis.
