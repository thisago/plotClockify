#!/usr/bin/env python3

import sys
from plot import read_csv, plot_box
from datetime import datetime


def prepare_day_data(rows):
    """Prepares day labels and data for plotting."""
    days = {}
    for row in rows:
        project = row["Project"]
        if project not in days:
            days[project] = {}
        day = row["Start Date"]
        try:
            duration = float(row["Duration (decimal)"])
            if day not in days[project]:
                days[project][day] = 0
            if day not in days[project]:
                days[project][day] = 0
            days[project][day] += duration
        except ValueError:
            print(f"Skipping invalid duration value: {row['Duration (decimal)']}")

    labels = list(set(day for email_days in days.values() for day in email_days.keys()))
    valid_labels = []
    for day in labels:
        try:
            try:
                valid_labels.append(f"{day} ({datetime.strptime(day, '%m/%d/%Y').strftime('%a')})")
            except ValueError:
                try:
                    valid_labels.append(f"{day} ({datetime.strptime(day, '%d/%m/%Y').strftime('%a')})")
                except ValueError:
                    print(f"Skipping invalid date value: {day}")
        except ValueError:
            print(f"Skipping invalid date value: {day}")
    labels = sorted(valid_labels, key=lambda x: datetime.strptime(x.split(" ")[0], '%d/%m/%Y'))
    stack_labels = list(days.keys())
    data = [
        [
            days[email].get(day.split(" ")[0], 0)  # Use only the date part of the label
            for day in labels
        ]
        for email in stack_labels
    ]
    return labels, data, stack_labels


# Main script
if len(sys.argv) < 2:
    print("Usage: python3 plot_days.py <csv_file>")
    sys.exit(1)

csv_file = sys.argv[1]
rows = read_csv(csv_file)
labels, data, stack_labels = prepare_day_data(rows)
plot_box(labels, data, stack_labels, "Daily Duration Distribution", "Days", "Total Duration (hours)")
