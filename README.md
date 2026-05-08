<h1 align="center">National Programme Operations Dashboard</h1>

<p align="center">
Operational analytics dashboard built in Power BI using a simulated national programme dataset generated with Python.
</p>

<p align="center">
  <img src="dashboard/dashboard_overview.png" width="950"/>
</p>

---

## Project Overview

This project is a simulated national programme operations analytics environment built using Python and Power BI. The solution models operational reporting workflows across large-scale digital training and engagement programmes, with a focus on learner participation, programme performance, engagement tracking, and regional monitoring.

The dashboard combines a multi-table relational data model with operational KPI reporting to provide executive-level visibility into programme delivery and learner engagement trends.

---

## Objectives

The dashboard was designed to:

- Monitor learner participation across programmes and regions
- Track operational KPIs such as completion rate and engagement performance
- Analyse demographic participation patterns
- Support programme performance and operational decision-making
- Simulate real-world monitoring and evaluation reporting workflows

---

## Tools & Technologies

<p>
  <img src="https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />
</p>

---

## Dataset Structure

The dataset was generated programmatically in Python and structured as a relational model consisting of:

### 1. Learners Table

Contains learner demographic and profile information including:

- Gender
- Age Group
- State of Origin
- State of Residence
- Education Level
- Employment Status
- Internet Quality
- Registration Source

### 2. Programmes Table

Contains programme-level operational information including:

- Programme Type
- Provider
- Programme Duration
- Start & End Dates
- Participant Targets

### 3. Programme Participation Table

Contains transactional participation-level records including:

- Engagement Score
- Attendance Rate
- Quiz Score
- Completion Status
- Dropout Reason
- Risk Level
- Programme Participation Activity

The final dataset simulates over 1 million participation records across multiple programme categories and operational dimensions.

---

## Dashboard Features

### Executive KPI Monitoring

- Learners Reached
- Programme Engagements
- Programme Completion Rate
- Average Engagement Score
- Active Programmes

### Operational Monitoring

- Monthly Participation Trend Analysis
- Programme Participation Mix
- Completion Status Distribution
- Regional Participation Analysis
- Top Participating States

### Learner Insights

- Gender Distribution
- Age Group Distribution
- Engagement Monitoring

### Interactive Filtering

The dashboard includes interactive slicers for:

- Year
- Provider
- Programme Type

---

## Dashboard Preview

<div align="center">
  <img src="dashboard/dashboard_overview.png" width="1000"/>
</div>

---

## Project Workflow

1. Generated a large-scale simulated operational dataset using Python
2. Structured the dataset into a relational model
3. Imported and modelled the data in Power BI
4. Created KPI measures using DAX
5. Designed an executive operational dashboard for programme monitoring and reporting

---

## Key Analytical Themes

- Programme Operations
- Learner Engagement
- Participation Trends
- Regional Performance
- Monitoring & Evaluation
- Operational Reporting

---

## Repository Structure

```text
national-programme-operations-dashboard/
│
├── dashboard/
│   ├── dashboard_overview.png
│
├── scripts/
│   ├── generate_dataset.py
│
├── README.md
├── requirements.txt
