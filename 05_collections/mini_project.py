sales = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 25},
    {"product": "Keyboard", "price": 80},
    {"product": "Monitor", "price": 350},
    {"product": "Headphones", "price": 150}
]

print("=== SALES REPORT ===")

# total sales
total = 0

for item in sales:
    total += item["price"]

print("Total revenue:", total)

# average price
average = total / len(sales)
print("Average product price:", round(average, 2))

# most expensive product
max_price = 0
most_expensive = ""

for item in sales:
    if item["price"] > max_price:
        max_price = item["price"]
        most_expensive = item["product"]

print("Most expensive product:", most_expensive, "-", max_price)

# cheapest product
min_price = sales[0]["price"]
cheapest_product = sales[0]["product"]

for item in sales:
    if item["price"] < min_price:
        min_price = item["price"]
        cheapest_product = item["product"]

print("Cheapest product:", cheapest_product, "-", min_price)

print("====================")