#!/usr/bin/env python3
import os
import sys
import csv
import plotext as plt


def read_csv(csv_file):
    """Reads the CSV file and returns its rows."""
    if not os.path.exists(csv_file):
        print(f"Error: File '{csv_file}' does not exist.")
        sys.exit(1)
    with open(csv_file, newline="") as file:
        return list(csv.DictReader(file))


def plot_box(labels, data, title, xlabel, ylabel):
    """Plots a box plot with the given labels and data."""
    if all(len(d) > 0 for d in data):
        plt.bar(labels, [sum(d) for d in data], width=0.3, orientation="vertical")
    else:
        print("No valid data to plot.")
        sys.exit(1)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
