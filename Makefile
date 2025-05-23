# Makefile to run the plot script

# Variables
PYTHON := python3
SCRIPT := ./src/plot.py
DATA ?= data/sample.csv

# Default target
run:
	@echo "Running script with data file: $(DATA)"
	$(PYTHON) $(SCRIPT) $(DATA)

# Clean target (optional, if needed for other tasks in the future)
clean:
	@echo "Nothing to clean for now."
