# Git Repository Analysis using PyDriller

This repository contains a Python script that utilizes the PyDriller library to analyze the commit history and various metrics of a specified Git repository. 

## Requirements

Before running the script, make sure you have the following Python packages installed:
- `pydriller`
- `python`

You can install them using pip:
```sh
pip install pydriller
pydriller official documentation: https://pydriller.readthedocs.io/en/latest/intro.html#

Run the script using
python3 drillcommit.py

Script Overview
The script performs the following analyses on the specified repository:

Traverse All Commits: Prints details of all commits in the repository.
Analyze Single Commit: Prints details of a specific commit.
Commits Since a Specific Date: Prints details of commits since 24/03/2020.
Commits Between Two Dates: Prints details of commits between two specified dates.
Commits in Master Branch: Prints details of commits only in the master branch.
Non-Merge Commits in Master Branch: Prints details of non-merge commits in the master branch.
Commits by a Specific Author: Prints details of commits by a specified author.
Specific Commits: Prints details of specified commits.
Commits Modifying HTML Files: Prints details of commits that modified HTML files.
Modified Files: Prints details of modified files in each commit.
Process Metrics: Computes and prints change set metrics.
Code Churn Metrics: Computes and prints code churn metrics (commented out).
Contributors Count: Computes and prints the number of contributors per file.
Lines Count: Computes and prints the total, maximum, and average lines added per file.

