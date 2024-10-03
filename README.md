
# Vanguard A/B Test Project

## Introduction

Welcome to the **Vanguard A/B Test Project**! This project is part of a Data Analytics Bootcamp and focuses on analyzing the results of a digital experiment conducted by Vanguard, a leading investment management company. Throughout this project, we will apply various data analytics techniques, including **Exploratory Data Analysis (EDA)**, **Data Cleaning**, **Performance Metrics**, **Hypothesis Testing**, **Experiment Evaluation**, and **Data Visualization** with Tableau.

## Project Context

As a newly employed data analyst in Vanguard's **Customer Experience (CX) Team**, you are tasked with analyzing the results of an A/B test. The test was conducted to evaluate whether a redesigned, more intuitive user interface (UI) and timely in-context prompts would improve the user experience and encourage more clients to complete Vanguard’s online process.

### The Experiment

- **Control Group**: Clients interacted with Vanguard's traditional online process.
- **Test Group**: Clients experienced the new digital interface with in-context prompts.
- **Objective**: Determine if the new design leads to higher process completion rates.

The experiment ran from **3/15/2017 to 6/20/2017** and involved multiple steps, starting from an initial page, through three process steps, to a final confirmation page.

## Datasets

Three datasets were provided to conduct the analysis:

1. **Client Profiles (df_final_demo)**: Demographic information about Vanguard’s clients.
2. **Digital Footprints (df_final_web_data)**: Client online interactions, split into two parts (pt_1 and pt_2). These datasets need to be merged for analysis.
3. **Experiment Roster (df_final_experiment_clients)**: Identifies which clients participated in the experiment.

## Project Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/mjimcode/vanguard-ab-test.git
   ```
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter notebooks or Python scripts to reproduce the analysis.

## Files in the Repository

- `vanguard-ab-test.ipynb`: The main Jupyter notebook containing the project analysis.
- `functions.py`: A Python file containing the functions used throughout the analysis.
- `tableau_dashboard.twb`: Tableau file with the visualizations created for the project.
- `README.md`: This file, which contains an overview of the project and instructions for running the analysis.

## Deliverables

1. **Jupyter Notebooks** with the analysis.
2. **Python scripts** for reusable functions (`functions.py`).
3. **Tableau dashboard** visualizing the findings.

## Conclusion

This project assesses whether Vanguard’s new UI design led to higher completion rates using statistical analysis, performance metrics, and hypothesis testing. Through data visualization in Tableau, we aim to provide clear insights into user behavior and the effectiveness of the redesign.
