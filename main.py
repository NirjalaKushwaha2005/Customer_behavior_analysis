import pandas as pd

df = pd.read_csv("customer_shopping_behavior.csv")

df.head()
df.info()
df.describe(include="all")
df.isnull().sum()

# Fill missing Review Rating using category median
df["Review Rating"] = df.groupby("Category")["Review Rating"].transform(
    lambda x: x.fillna(x.median())
)

df.isnull().sum()

# Convert column names to lowercase
df.columns = df.columns.str.lower()

# Replace spaces with underscore
df.columns = df.columns.str.replace(" ", "_")

df = df.rename(columns={"purchase_amount_(usd)": "purchase_amount"})

print(df.columns)
# Create age group
labels = ["young adult", "adult", "middle-aged", "senior"]

df["age_group"] = pd.qcut(
    df["age"],
    q=4,
    labels=labels
)

print(df[["age", "age_group"]].head(10))
# Create purchase frequency in days
frequency_mapping = {
    "Fortnightly": 14,
    "Weekly": 7,
    "Monthly": 30,
    "Quarterly": 90,
    "Bi-Weekly": 14,
    "Annually": 365,
    "Every 3 Months": 90
}

df["purchase_frequency_days"] = df["frequency_of_purchases"].map(frequency_mapping)

print(df[["frequency_of_purchases", "purchase_frequency_days"]].head(10))
# Create discount_applied column
df["discount_applied"] = df["promo_code_used"]

print(df[["discount_applied", "promo_code_used"]].head(10))

# Check whether both columns contain the same values
print((df["discount_applied"] == df["promo_code_used"]).all())
# Remove duplicate column
df = df.drop("promo_code_used", axis=1)

print(df.columns)
# Check final dataset
print(df.head())
print(df.info())

# Save cleaned data
df.to_csv("customer_shopping_behavior_cleaned.csv", index=False)

print("Cleaned data saved successfully!")