import pandas as pd

# 1. Create a database where Continental AG is duplicated (row 0 and row 3 are identical)
supplier_data = {
    "Supplier_Name": ["Continental AG", "Bosch GmbH", "Steel-Plast s.r.o.", "Continental AG"],
    "Country": ["Germany", "Germany", "Slovakia", "Germany"]
}

df = pd.DataFrame(supplier_data)

print("--- ORIGINAL TABLE (WITH DUPLICATES) ---")
print(df)
print("\n")

# 2. We drop the duplicate rows
cleaned_df = df.drop_duplicates()

print("--- CLEANED TABLE (NO DUPLICATES) ---")
print(cleaned_df)