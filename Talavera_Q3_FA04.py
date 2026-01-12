names = ["Me", "Lia", "Jake"]

steps = [
    [4500, 5200, 4800, 5000, 5300],   # Me
    [4000, 4100, 3900, 4200, 4600],   # Lia
    [6000, 5800, 5900, 6100, 6200]    # Jake
]

totals = []

for i in range(len(steps)):
    total_steps = sum(steps[i])
    totals.append(total_steps)
    print(names[i], "total steps:", total_steps)

highest = max(totals)
lowest = min(totals)

top_index = totals.index(highest)
top_person = names[top_index]

print("\nTop performer:", top_person)
print("Highest total steps:", highest)
print("Lowest total steps:", lowest)
print("Difference between highest and lowest:", highest - lowest)
