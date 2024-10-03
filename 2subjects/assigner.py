import csv
import numpy as np
from scipy.optimize import linear_sum_assignment

unique_subjects = [
    "انواع ارائه و ملزومات آن",
    "ابزارهای تولید کننده هوش مصنوعی - ChatGPT",
    "ابزارهای تولید کننده هوش مصنوعی - Gemini",
    "ابزارهای تولید کننده هوش مصنوعی - ClaudeAI",
    "ابزارهای تولید کننده هوش مصنوعی - DALL-E",
    "ابزار های تقلب‌یاب - Turnitin",
    "ابزارهای ارائه موثر - Canva",
    "ابزارهای ارائه موثر - Prezi",
    "ابزار های تقلب‌یاب - Unicheck",
    "ابزار های تقلب‌یاب - Proctoru",
    "ابزار های تقلب‌یاب - MOSS",
    "ابزار های تقلب‌یاب - Plagscan",
    "ابزارهای تولید کننده هوش مصنوعی - Llama",
    "ابزار های ارجاع دهی - Zotero",
    "ابزار های ارجاع دهی - Mendeley",
    "ابزار های ارجاع دهی"
]


# Read priority lists from the CSV file
def read_priority_lists_from_csv(filename):
    people_preferences = []
    with open(filename, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header
        for row in csv_reader:
            # Convert the priority list string back to list of integers
            priority_list = list(map(int, row[1].split(',')))
            people_preferences.append(priority_list)
    return people_preferences

# Function to create cost matrix (same as before)
def create_cost_matrix(people_preferences, n):
    cost_matrix = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            try:
                cost_matrix[i][j] = people_preferences[i].index(j + 1)  # Adjusting to 1-based indexing
            except:
                cost_matrix[i][j] = len(unique_subjects) -1
    return cost_matrix

# Function to assign people to subjects (same as before)
def assign_people_to_subjects(people_preferences, n):
    cost_matrix = create_cost_matrix(people_preferences, n)
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    return list(zip(row_ind, col_ind))

# Load people preferences from CSV
people_preferences = read_priority_lists_from_csv('priority_lists.csv')

# Number of people/groups
n = len(people_preferences)

# Assign people to subjects
assignments = assign_people_to_subjects(people_preferences, n)

# Print assignments
for person, subject in assignments:
    print(f"Person {person + 1} is assigned to subject {subject + 1}")
    print(unique_subjects[subject])
    print("____________")
