# Smart Finance & Sales Analytics System

import csv
import os
import json

FILE = "sales.csv"

# Step 1: Create CSV file if not exists
if not os.path.exists(FILE):
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Product", "Units", "Revenue", "Cost"])

        # Sample data
        writer.writerow(["01-02-2026", "Laptop", 5, 50000, 35000])
        writer.writerow(["02-02-2026", "Phone", 10, 30000, 18000])
        writer.writerow(["03-02-2026", "Tablet", 3, 15000, 9000])

print("CSV ready")

# Step 2: Read + calculate profit
def read_data():
    records = []

    with open(FILE) as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["Units"] = int(row["Units"])
            row["Revenue"] = float(row["Revenue"])
            row["Cost"] = float(row["Cost"])
            row["Profit"] = row["Revenue"] - row["Cost"]
            records.append(row)

    return records

# Step 3: Financial Summary
def financial_summary():
    data = read_data()

    if not data:
        print("No Sales Found.")
        return

    total_revenue = sum(r["Revenue"] for r in data)
    total_cost = sum(r["Cost"] for r in data)
    total_profit = sum(r["Profit"] for r in data)

    print("\n====== FINANCIAL SUMMARY ======")
    print(f"Total Revenue: ₹{total_revenue:.2f}")
    print(f"Total Cost: ₹{total_cost:.2f}")
    print(f"Total Profit: ₹{total_profit:.2f}")

    ranked = sorted(data, key=lambda x: x["Profit"], reverse=True)

    print("\n--- Product Profit Ranking ---")
    for i, r in enumerate(ranked, start=1):
        print(f"{i}. {r['Product']} - Profit: ₹{r['Profit']:.2f}")

# Step 4: Add Sale
def add_sale():
    date = input("Date (DD-MM-YYYY): ")
    product = input("Product name: ")

    try:
        units = int(input("Units Sold: "))
        revenue = float(input("Revenue: "))
        cost = float(input("Cost: "))
    except ValueError:
        print("Invalid number entered.")
        return

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, product, units, revenue, cost])

    print("Sales record added successfully!\n")

# Step 5: Insight Generator
def generate_insights():
    data = read_data()

    if not data:
        print("No data available.")
        return

    total_profit = sum(r["Profit"] for r in data)
    top_revenue = max(data, key=lambda x: x["Revenue"])
    lowest_profit = min(data, key=lambda x: x["Profit"])

    print("\n==== BUSINESS INSIGHTS ====")
    print(f"Total Profit Generated: ₹{total_profit:.2f}")
    print(f"Top Revenue Product: {top_revenue['Product']}")
    print(f"Lowest Profit Product: {lowest_profit['Product']}")

    if lowest_profit["Profit"] < 0:
        print("⚠ Warning: Some products are generating losses!")

# Step 6: Export JSON
def export_report():
    data = read_data()

    total_revenue = sum(r["Revenue"] for r in data)
    total_cost = sum(r["Cost"] for r in data)
    total_profit = sum(r["Profit"] for r in data)

    report = {
        "total_revenue": total_revenue,
        "total_cost": total_cost,
        "total_profit": total_profit,
        "records": data
    }

    with open("business_report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("Report exported to business_report.json\n")

# Step 7: Menu
def menu():
    while True:
        print("\n======= SMART BUSINESS ANALYTICS =======")
        print("1. Add Sale")
        print("2. Financial Summary")
        print("3. Generate Insights")
        print("4. Export Report")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_sale()
        elif choice == "2":
            financial_summary()
        elif choice == "3":
            generate_insights()
        elif choice == "4":
            export_report()
        elif choice == "5":
            print("Exiting system...")
            break
        else:
            print("Invalid choice")

menu()