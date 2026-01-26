# 2D array from Activity 1 (scores of 3 students in 4 subjects)
scores = [
    [85, 90, 88, 92],
    [78, 84, 80, 86],
    [90, 95, 93, 89]
]

# Print each row and calculate total and average
for i in range(len(scores)):
    print("Student", i + 1, "scores:", scores[i])

    total = sum(scores[i])
    average = total / len(scores[i])

    print("Total:", total)
    print("Average:", average)
    print()

# Find the maximum score in the entire dataset
highest = scores[0][0]

for row in scores:
    for value in row:
        if value > highest:
            highest = value

print("Highest score in the dataset:", highest)

Short Explanation (3–4 sentences)
Using a 2D array made it easier to organize the data because each row represents one student and their scores. It allowed me to use loops to calculate totals and 
averages without repeating code. Calculating the total and average for each row was easy using the sum() function. 
Finding the highest value was a bit harder because it required checking each value one by one.

