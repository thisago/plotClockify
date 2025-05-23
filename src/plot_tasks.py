#!/usr/bin/env python3

import sys
from plot import read_csv, plot_box


def prepare_task_data(rows):
    """Prepares task labels and data for plotting."""
    tasks = {}  # Dictionary to store task data grouped by email
    emails = set(row["Email"] for row in rows)  # Collect unique emails
    for row in rows:  # Iterate rows
        email = row["Email"]
        if email not in tasks:
            tasks[email] = {}
        task = row["Description"]
        try:
            duration = float(row["Duration (decimal)"])
            if task not in tasks[email]:
                tasks[email][task] = 0
            tasks[email][task] += duration
        except ValueError:
            print(f"Skipping invalid duration value: {row['Duration (decimal)']}")

    labels = sorted(set(task for email_tasks in tasks.values() for task in email_tasks.keys()))
    stack_labels = list(tasks.keys())
    data = [
        [tasks[email].get(task, 0) for task in labels]
        for email in stack_labels
    ]
    return labels, data, stack_labels


# Main script
if len(sys.argv) < 2:
    print("Usage: python3 plot_tasks.py <csv_file>")
    sys.exit(1)

csv_file = sys.argv[1]
rows = read_csv(csv_file)
labels, data, stack_labels = prepare_task_data(rows)
plot_box(labels, data, stack_labels, "Task Duration Distribution", "Task Names", "Duration (hours)")
