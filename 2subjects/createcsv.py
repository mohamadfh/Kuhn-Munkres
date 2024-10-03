import csv

# Priority lists for each group (based on the input provided)
priority_lists = [
    ["Group 1", "1, 2, 3, 4, 5, 6, 7, 8"],
    ["Group 2", "1, 2, 3, 4, 5, 6, 7, 8"],
    ["Group 3", "1, 2, 3, 6, 5, 7, 4, 8"],
    ["Group 4", "1, 4, 3, 6, 5, 7, 8, 9"],
    ["Group 5", "2, 1, 9, 7, 8, 4, 5, 6"]
]

# Write priority lists to CSV file
with open('priority_lists.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Group", "Priority List"])  # Header
    for group, priority_list in priority_lists:
        writer.writerow([group, priority_list])

print("Priority lists have been written to priority_lists.csv")
