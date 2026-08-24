import pandas as pd
import os

def run_shipment_analysis():
    print("=== STARTING SHIPMENT PERFORMANCE ANALYZER ===")

    # 1. Simulate Raw, Uncleaned Shipment Data (Dirty supplier names & dates as text)
    raw_shipment_data = {
        "Supplier_Name": [" Continental AG", "Bosch GmbH ", "Steel-Plast s.r.o.", " Continental AG", "Bosch GmbH "],
        "Order_Date": ["2026-08-01", "2026-08-02", "2026-08-05", "2026-08-10", "2026-08-12"],
        "Delivery_Date": ["2026-08-05", "2026-08-11", "2026-08-07", "2026-08-13", "2026-08-22"]
    }
    
    # Load into DataFrame
    df = pd.DataFrame(raw_shipment_data)
    print("\n[STEP 1] Raw Logistics Data Loaded:")
    print(df)

    # 2. Clean Supplier Names (Remove accidental whitespace)
    df['Supplier_Name'] = df['Supplier_Name'].str.strip()
    print("\n[STEP 2] Supplier Names Cleaned (Spaces Removed).")

    # 3. Convert Dates and Calculate Shipping Duration (Lead Time in Days)
    df['Order_Date'] = pd.to_datetime(df['Order_Date'])
    df['Delivery_Date'] = pd.to_datetime(df['Delivery_Date'])
    df['Shipping_Days'] = (df['Delivery_Date'] - df['Order_Date']).dt.days
    print("\n[STEP 3] Dates Converted & Shipping Duration (Lead Time) Calculated:")
    print(df)

    # 4. Group by Supplier and Calculate average lead time
    performance_report = df.groupby('Supplier_Name')['Shipping_Days'].mean().round(1).reset_index()
    # Rename columns for clarity
    performance_report.columns = ['Supplier_Name', 'Average_Lead_Time_Days']
    # Sort from fastest to slowest
    performance_report = performance_report.sort_values(by='Average_Lead_Time_Days')
    
    print("\n[STEP 4] Final Performance Report (Average Lead Time per Supplier):")
    print(performance_report)

    # 5. Export finalized report to CSV
    output_folder = "12_mini_projects"
    output_path = os.path.join(output_folder, "shipment_performance_report.csv")
    
    performance_report.to_csv(output_path, index=False)
    print(f"\n[STEP 5] Success! Finalized report exported to: '{output_path}'")
    print("=============================================")

if __name__ == '__main__':
    run_shipment_analysis()