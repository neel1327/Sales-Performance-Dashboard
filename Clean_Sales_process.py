import pandas as pd

# Load dataset
df = pd.read_csv("Sample - Superstore.csv", encoding='latin1')

# Check missing values
print("Missing values:\n", df.isnull().sum())

# Convert date columns
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Create Delivery Days column
df['Delivery Days'] = (df['Ship Date'] - df['Order Date']).dt.days

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned file
df.to_csv("cleaned_sales.csv", index=False)

print("Cleaned file created!")