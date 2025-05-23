#!/usr/bin/env python3

import sys
from plot import read_csv, plot_box


def prepare_day_data(rows):
    """Prepares day labels and data for plotting."""
    days = {}
    for row in rows:
        day = row["Start Date"]
        try:
            duration = float(row["Duration (decimal)"])
            if day not in days:
                days[day] = 0
            days[day] += duration
        except ValueError:
            print(f"Skipping invalid duration value: {row['Duration (decimal)']}")

    labels = list(days.keys())
    # Ensure all data lists have at least five elements by padding with the same value
    data = [[days[label]] * 5 for label in labels]
    return labels, data


# Main script
if len(sys.argv) < 2:
    print("Usage: python3 plot_days.py <csv_file>")
    sys.exit(1)

csv_file = sys.argv[1]
rows = read_csv(csv_file)
labels, data = prepare_day_data(rows)
plot_box(labels, data, "Daily Duration Distribution", "Days", "Total Duration (hours)")
