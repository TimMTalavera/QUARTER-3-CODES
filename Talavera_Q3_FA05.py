names = ["Me", "Lia", "Jake"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = [
    [4500, 5200, 4800, 5000, 5300],   # Me
    [4000, 4100, 3900, 4200, 4600],   # Lia
    [6000, 5800, 5900, 6100, 6200]    # Jake
]

highest_total = 0
most_active_day = ""

# Loop by column (day)
for d in range(len(days)):
    daily_total = 0

    # Add steps from each person for that day
    for p in range(len(steps)):
        daily_total = daily_total + steps[p][d]

    print(days[d], "total steps:", daily_total)

    if daily_total > highest_total:
        highest_total = daily_total
        most_active_day = days[d]

print("\nMost active day overall:", most_active_day)
print("Highest total steps in a day:", highest_total)
