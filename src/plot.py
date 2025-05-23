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


def plot_box(labels, data, stack_labels, title, xlabel, ylabel):
    """Plots a stacked bar plot with the given labels and data."""
    if all(len(d) > 0 for d in data):
        plt.simple_stacked_bar(labels, data, labels=stack_labels)
    else:
        print("No valid data to plot.")
        sys.exit(1)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
