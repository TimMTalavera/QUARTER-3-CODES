Python code
prices = [
    [52, 50, 55],    # Rice
    [75, 72, 78],    # Milk
    [45, 48, 46],    # Bread
    [8, 9, 8.5],     # Eggs
    [12, 11, 13]     # Apples
]

items = ["Rice", "Milk", "Bread", "Eggs", "Apples"]

# Print each row clearly and compute total and average
for i in range(len(prices)):
    row = prices[i]
    total = sum(row)
    average = total / len(row)
    print(items[i], "prices:", row)
    print("  Total:", total)
    print("  Average:", average)

# Find maximum and minimum price in the entire dataset
max_price = max(max(row) for row in prices)
min_price = min(min(row) for row in prices)

print("\nHighest price in dataset:", max_price)
print("Lowest price in dataset:", min_price)

Sample Output
Rice prices: [52, 50, 55]
  Total: 157
  Average: 52.33
Milk prices: [75, 72, 78]
  Total: 225
  Average: 75.0
Bread prices: [45, 48, 46]
  Total: 139
  Average: 46.33
Eggs prices: [8, 9, 8.5]
  Total: 25.5
  Average: 8.5
Apples prices: [12, 11, 13]
  Total: 36
  Average: 12.0

Highest price in dataset: 78
Lowest price in dataset: 8
