# ==========================================
# 1. LIST COMPREHENSIONS VS TRADITIONAL FOR LOOPS
# ==========================================
print("=== ADVANCED TOPIC 1: List Comprehensions ===")

# Traditional way: Let's double the lead times of these shipments
lead_times = [2, 5, 8, 3, 10]
doubled_times = []
for t in lead_times:
    doubled_times.append(t * 2)
print("Traditional Loop Result:", doubled_times)

# Advanced way (List Comprehension - 1 line!):
doubled_times_advanced = [t * 2 for t in lead_times]
print("List Comprehension Result:", doubled_times_advanced)

# Filtering with List Comprehension (Only keep delayed lead times > 5 days)
delayed_shipments = [t for t in lead_times if t > 5]
print("Filtered Delayed Shipments (> 5 days):", delayed_shipments)
print("\n")


# ==========================================
# 2. LAMBDA FUNCTIONS (Quick Calculations)
# ==========================================
print("=== ADVANCED TOPIC 2: Lambda Functions ===")

# Standard function
def standard_add_vat(price):
    return price * 1.20

# Lambda function doing the exact same thing
lambda_add_vat = lambda price: price * 1.20

print("Standard Function VAT price:", standard_add_vat(100))
print("Lambda Function VAT price:", lambda_add_vat(100))
print("\n")


# ==========================================
# 3. ZIP & ENUMERATE (Logistics Helpers)
# ==========================================
print("=== ADVANCED TOPIC 3: Zip and Enumerate ===")

suppliers = ["Continental AG", "Bosch GmbH", "Steel-Plast s.r.o."]
ratings = [95, 88, 92]

# Enumerate: Loop with index and value
print("Using Enumerate (Listing active partners with rank):")
for index, supplier in enumerate(suppliers, start=1):
    print(f"Rank {index}: {supplier}")

print("\nUsing Zip (Pairing suppliers with their compliance ratings):")
# Zip: Pairing two lists side-by-side
for supplier, rating in zip(suppliers, ratings):
    print(f"Supplier: {supplier} | ESG Rating: {rating}%")
