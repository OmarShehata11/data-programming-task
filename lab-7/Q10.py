# Initialize department names and available items
departments = ["Meat", "Seafood", "Milk", "Bread", "Oil"]
available_items = {}

# Take input from the stock clerk for available items in each department
for department in departments:
    available = int(input(f"How many available items in {department}? "))
    available_items[department] = available

# Initialize department prices
prices = {}

# Take input from the stock clerk for prices of available items in each department
for department in departments:
    price = float(input(f"What are the prices of the available items in {department}? "))
    prices[department] = price

# Initialize promo code
promo_code = "123456"

# Initialize variables for total sales and department sales
total_sales = 0
department_sales = {department: 0 for department in departments}

# Initialize variables for calculating ratios
total_sold_items = 0
department_sold_items = {department: 0 for department in departments}

# Working hours
working_hours = 13  # 8AM to 9PM

while working_hours > 0:
    if sum(available_items.values()) == 0:
        print("No items left in the store. The store is closed.")
        break

    customer_order = {}
    for department in departments:
        num_items = int(input(f"How many you want from {department}? "))
        if num_items > available_items[department]:
            num_items = available_items[department]
        customer_order[department] = num_items

        if department == "Milk":
            promo = input("Please enter promo if you have: ")
            if promo == promo_code:
                customer_order[department] -= num_items * 0.3
                print("Promo code applied: 30% discount on Milk")

        total_sales += customer_order[department] * prices[department]
        department_sales[department] += customer_order[department]
        total_sold_items += customer_order[department]
        department_sold_items[department] += customer_order[department]
        available_items[department] -= customer_order[department]

    print(f"Dear prospective customer, the total is: {total_sales:.1f} pounds")
    working_hours -= 1

# Generate and print the report
print("We sold today:")
sorted_departments = sorted(department_sold_items, key=lambda d: department_sold_items[d] / total_sold_items)
for department in sorted_departments:
    ratio = (department_sold_items[department] / total_sold_items) * 100
    print(f"{ratio:.2f}% {department}")

