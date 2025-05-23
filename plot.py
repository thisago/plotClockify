#!/usr/bin/env python3

import sys
import csv
import plotext as plt

# Check if the file name is provided as a parameter
if len(sys.argv) < 2:
    print("Usage: python3 script.py <csv_file>")
    sys.exit(1)

# Read the CSV file from the command-line argument
csv_file = sys.argv[1]
tasks = {}
with open(csv_file, newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        task = row["Task"]
        duration = float(row["Duration (decimal)"])
        if task not in tasks:
            tasks[task] = []
        tasks[task].append(duration)

# Prepare data for the box plot
labels = list(tasks.keys())
data = [tasks[label] for label in labels]

# Plot the data
plt.box(labels, data, width=0.3, quintuples=True)
plt.title("Task Duration Distribution")
plt.xlabel("Tasks")
plt.ylabel("Duration (hours)")
plt.show()
