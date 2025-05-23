#!/usr/bin/env python3

import sys
from plot import read_csv, plot_box


def prepare_task_data(rows):
    """Prepares task labels and data for plotting."""
    tasks = {}
    for row in rows:
        task = row["Task"]
        try:
            duration = float(row["Duration (decimal)"])
            if task not in tasks:
                tasks[task] = []
            tasks[task].append(duration)
        except ValueError:
            print(f"Skipping invalid duration value: {row['Duration (decimal)']}")

    labels = [label for label in tasks.keys() if len(tasks[label]) > 0]
    data = [
        (
            tasks[label] + [tasks[label][-1]] * (5 - len(tasks[label]))
            if len(tasks[label]) < 5
            else tasks[label]
        )
        for label in labels
    ]
    return labels, data


# Main script
if len(sys.argv) < 2:
    print("Usage: python3 plot_tasks.py <csv_file>")
    sys.exit(1)

csv_file = sys.argv[1]
rows = read_csv(csv_file)
labels, data = prepare_task_data(rows)
plot_box(labels, data, "Task Duration Distribution", "Tasks", "Duration (hours)")
