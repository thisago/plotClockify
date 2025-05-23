# Makefile to run the plot scripts

# Variables
PYTHON := python3
TASK_SCRIPT := ./src/plot_tasks.py
DAY_SCRIPT := ./src/plot_days.py
DATA ?= data/sample.csv

# Targets
run-tasks:
	@echo "Running task plot script with data file: $(DATA)"
	$(PYTHON) $(TASK_SCRIPT) $(DATA)

run-days:
	@echo "Running day plot script with data file: $(DATA)"
	$(PYTHON) $(DAY_SCRIPT) $(DATA)

clean:
	@echo "Nothing to clean for now."
