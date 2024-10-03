import csv

# Priority lists for groups (based on the order provided)
priority_lists = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 7, 5, 6, 8],
    [1, 4, 3, 6, 5, 7, 8, 9]
]

# Writing priority lists to CSV
with open('priority_lists.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Group", "Priority List"])
    for idx, priority_list in enumerate(priority_lists):
        writer.writerow([f"Group {idx + 1}", ",".join(map(str, priority_list))])

print("Priority lists have been written to priority_lists.csv")
