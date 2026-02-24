import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")

print("Original Data:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Drop rows with missing values
df = df.dropna()

# Remove duplicates
df = df.drop_duplicates()

# Create Total Column
df["Total"] = df["Quantity"] * df["Price"]

# Total Revenue
total_revenue = df["Total"].sum()
print("\nTotal Revenue:", total_revenue)

# City-wise Revenue
city_sales = df.groupby("City")["Total"].sum()
print("\nCity-wise Revenue:")
print(city_sales)

# Save cleaned data
df.to_csv("cleaned_sales_data.csv", index=False)

print("\nCleaned Data Saved Successfully!")