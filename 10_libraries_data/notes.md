# 10 – Libraries & Data (Pandas Basics)

## 1. What is Pandas? 🐼

Pandas is a Python library used for working with data. 

Think about real life:
- You have a huge Excel sheet with thousands of rows.
- Opening it in Excel is slow and manual.
- **Pandas** is like Excel on steroids, but inside Python. It is fast, powerful, and automates everything.

---

## 2. DataFrame (The Table)

A **DataFrame** is the main object in Pandas. 

Think of it as a standard table:
- It has **rows** (horizontal).
- It has **columns** (vertical).

```python
import pandas as pd

# Creating a simple DataFrame (table)
data = {
    'Supplier': ['Bosch', 'Continental'],
    'Rating': ['Compliant', 'Pending']
}
df = pd.DataFrame(data)
3. read_csv()
Normally, we don't type data manually. We load it from an external file (like a CSV or Excel).
read_csv() is a function that opens a CSV file and turns it into a Pandas DataFrame.
df = pd.read_csv('suppliers.csv')
4. head() – First Look
head() is a method that shows you the first rows of your table. By default, it shows the first 5 rows.
It is used to check if the data loaded correctly.
print(df.head())
5. info() – Technical Check
info() is a method that tells you the technical status of your table.
It shows:
How many rows you have.
What columns are in the table.
If there are any missing values (blank spaces/nulls).
What type of data is in each column (text, integers, decimals).
df.info()
6. isna() – Finding Blanks (None / NaN)
In Python, missing data is represented as NaN (Not a Number) or None.
isna() is a helper that checks every cell and returns True if the cell is empty (blank). We use it to filter out suppliers that haven't filled in their registration details yet.
# Finds rows where DUNS is blank
missing_duns = df[df['DUNS_Number'].isna()]
