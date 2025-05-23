#!/usr/bin/env python3

import sys
from plot import read_csv, plot_box


def prepare_day_data(rows):
    """Prepares day labels and data for plotting."""
    days = {}
    for row in rows:
        email = row["Email"]
        if email not in days:
            days[email] = {}
        day = row["Start Date"]
        try:
            duration = float(row["Duration (decimal)"])
            if day not in days[email]:
                days[email][day] = 0
            if day not in days[email]:
                days[email][day] = 0
            days[email][day] += duration
        except ValueError:
            print(f"Skipping invalid duration value: {row['Duration (decimal)']}")

    labels = list(set(day for email_days in days.values() for day in email_days.keys()))
    stack_labels = list(days.keys())
    data = [
        [days[email].get(day, 0) for day in labels]
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
