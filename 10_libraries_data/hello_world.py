import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg') # Pre bezproblémové uloženie grafu vo VS Code
import matplotlib.pyplot as plt

print("=== TOPIC 15: Dates & New Columns ===")
logistics_data = {
    "Supplier_Name": ["Continental AG", "Bosch GmbH", "Steel-Plast s.r.o."],
    "Order_Date": ["2026-08-01", "2026-08-03", "2026-08-10"],
    "Delivery_Date": ["2026-08-05", "2026-08-12", "2026-08-11"],
    "Rating_Text": ["95", "88", "92"] # Nateraz uložené ako text
}
df = pd.DataFrame(logistics_data)

# Convert to datetime and calculate Lead Time
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Delivery_Date'] = pd.to_datetime(df['Delivery_Date'])
df['Lead_Time_Days'] = (df['Delivery_Date'] - df['Order_Date']).dt.days
print(df)
print("\n")


print("=== TOPIC 16: loc vs iloc ===")
# loc uses NAMES
print("Using .loc (Row index 0, Column 'Supplier_Name'):")
print(df.loc[0, 'Supplier_Name'])

# iloc uses POSITION NUMBERS (0 is first row, 4 is Lead_Time_Days column index)
print("Using .iloc (Row position 0, Column position 4):")
print(df.iloc[0, 4])
print("\n")


print("=== TOPIC 17: .astype() ===")
# Check datatype of Rating_Text (it's object/string)
print("Before conversion:", df['Rating_Text'].dtype)

# Convert to integer
df['Rating_Text'] = df['Rating_Text'].astype(int)
print("After conversion:", df['Rating_Text'].dtype)
print("\n")


print("=== TOPIC 18: NumPy Arrays ===")
# Create a NumPy array from the Lead_Time_Days column
lead_times_array = np.array(df['Lead_Time_Days'])
print("NumPy Array of Lead Times:", lead_times_array)

# Quick math on the whole array
print("Lead Times in hours (multiplied by 24):", lead_times_array * 24)
print("\n")


print("=== TOPIC 19: Matplotlib Line Chart ===")
# Plot a simple trend chart of Lead Times
plt.plot(df['Supplier_Name'], df['Lead_Time_Days'], marker='o', color='green')
plt.title("Lead Time Trend by Supplier")
plt.ylabel("Days")
plt.savefig('10_libraries_data/lead_time_trend.png', bbox_inches='tight')
plt.close()
print("Success! Trend chart saved as 'lead_time_trend.png'.")