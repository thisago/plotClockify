#!/usr/bin/env python3

import sys
import csv
import plotext as plt
import os

# Check if the file name is provided as a parameter
if len(sys.argv) < 2:
    print("Usage: python3 script.py <csv_file>")
    sys.exit(1)


def read_and_prepare_data(csv_file):
    """Reads the CSV file and prepares labels and data for plotting."""
    tasks = {}
    if not os.path.exists(csv_file):
        print(f"Error: File '{csv_file}' does not exist.")
        sys.exit(1)
    with open(csv_file, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            task = row["Task"]
            try:
                duration = float(row["Duration (decimal)"])
                if task not in tasks:
                    tasks[task] = []
                tasks[task].append(duration)
            except ValueError:
                print(f"Skipping invalid duration value: {row['Duration (decimal)']}")

    # Prepare labels and data, filtering out empty data
    labels = [label for label in tasks.keys() if len(tasks[label]) > 0]
    # Ensure all data lists have at least five elements by padding with the last value
    data = [
        (
            tasks[label] + [tasks[label][-1]] * (5 - len(tasks[label]))
            if len(tasks[label]) < 5
            else tasks[label]
        )
        for label in labels
    ]
    return labels, data


# Read the CSV file and prepare data
csv_file = sys.argv[1]
labels, data = read_and_prepare_data(csv_file)

# Plot the data only if there is valid data
if all(len(d) > 0 for d in data):
    plt.box(labels, data, width=0.3, quintuples=True, orientation="vertical")
else:
    print("No valid data to plot.")
    sys.exit(1)

plt.title("Task Duration Distribution")
plt.xlabel("Tasks")
plt.ylabel("Duration (hours)")
plt.show()
