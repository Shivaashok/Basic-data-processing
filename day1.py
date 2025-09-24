import pandas as pd

# 1. Load dataset
df = pd.read_csv("sales_data.csv")

print("🔹 Original Shape:", df.shape)
print("🔹 Columns:", df.columns.tolist())

# 2. Handle missing values
print("\nMissing values before cleaning:\n", df.isnull().sum())

# Drop rows with all NaN values
df = df.dropna(how='all')

# Fill missing numeric values with median
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

# Fill missing categorical values with "Unknown"
cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    df[col] = df[col].fillna("Unknown")

# 3. Remove duplicates
df = df.drop_duplicates()

# 4. Standardize text values BEFORE renaming columns
if "PaymentMode" in df.columns:
    df["PaymentMode"] = df["PaymentMode"].astype(str).str.strip().str.lower()

if "Category" in df.columns:
    df["Category"] = df["Category"].astype(str).str.title()

if "Sub-Category" in df.columns:
    df["Sub-Category"] = df["Sub-Category"].astype(str).str.title()

if "State" in df.columns:
    df["State"] = df["State"].astype(str).str.title()

if "City" in df.columns:
    df["City"] = df["City"].astype(str).str.title()

# 5. Fix date formats
if "Order Date" in df.columns:
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors='coerce')

# 6. Rename columns (make them clean and uniform)
df.columns = df.columns.str.lower().str.replace(" ", "_")

# 7. Correct data types (safe casting)
if "amount" in df.columns:
    df["amount"] = df["amount"].astype(float)

if "profit" in df.columns:
    df["profit"] = df["profit"].astype(float)

if "quantity" in df.columns:
    df["quantity"] = df["quantity"].astype(int)

# 8. Save cleaned dataset
df.to_csv("sales_data_cleaned.csv", index=False)

print("\n🔹 Cleaned Shape:", df.shape)
print("✅ Cleaning complete. File saved as sales_data_cleaned.csv")
