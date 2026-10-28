
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "WA_Fn-UseC_-HR-Employee-Attrition.csv"
OUT_DIR = BASE_DIR / "outputs"
OUT_DIR.mkdir(exist_ok=True)

# 1. Import dataset
df = pd.read_csv(DATA_FILE)
print("Dataset loaded:", df.shape)

# 2. Check and clean missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum().sum())

for col in df.columns:
    if df[col].isnull().any():
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].median())
        else:
            mode = df[col].mode()
            df[col] = df[col].fillna(
                mode.iloc[0] if not mode.empty else "Unknown"
            )

print("Missing values after cleaning:", df.isnull().sum().sum())

# 3. Remove duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())
df = df.drop_duplicates().copy()

# 4. Detect outliers using IQR
numeric_cols = df.select_dtypes(include="number").columns
outliers = []

for col in numeric_cols:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    count = int(((df[col] < lower) | (df[col] > upper)).sum())

    outliers.append({
        "Feature": col,
        "Lower_Bound": lower,
        "Upper_Bound": upper,
        "Outlier_Count": count
    })

pd.DataFrame(outliers).to_csv(
    OUT_DIR / "outlier_summary.csv", index=False
)

# 5. Encode categorical variables
categorical_cols = df.select_dtypes(
    include=["object", "category", "bool"]
).columns.tolist()

encoded_df = pd.get_dummies(
    df, columns=categorical_cols, dtype=int
)

# Save output files
df.to_csv(OUT_DIR / "employee_attrition_cleaned.csv", index=False)
encoded_df.to_csv(
    OUT_DIR / "employee_attrition_cleaned_encoded.csv", index=False
)

summary = pd.DataFrame({
    "Metric": [
        "Rows after cleaning",
        "Columns before encoding",
        "Missing values after cleaning",
        "Duplicate rows after cleaning",
        "Categorical columns encoded",
        "Columns after encoding"
    ],
    "Value": [
        len(df),
        len(df.columns),
        int(df.isnull().sum().sum()),
        int(df.duplicated().sum()),
        len(categorical_cols),
        encoded_df.shape[1]
    ]
})
summary.to_csv(OUT_DIR / "preparation_report.csv", index=False)

print("\nSUCCESS! Data preparation completed.")
print("Check the outputs folder.")
