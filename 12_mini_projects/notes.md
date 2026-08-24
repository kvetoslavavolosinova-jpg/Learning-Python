# 12 - Mini Projects

## 1. What is a Mini-Project?
- A mini-project combines multiple programming concepts (Variables, Functions, Loops, File Handling, and Pandas) to solve a single, cohesive real-world problem.
- Instead of writing isolated code snippets, we build a structured, end-to-end data pipeline.

## 2. Project Overview: Shipment Performance Analyzer
- **Goal**: Help a logistics team evaluate transport partners by analyzing raw shipment logs.
- **Workflow**:
  1. **Data Ingestion**: Read raw, uncleaned shipment records containing order and delivery dates.
  2. **Data Cleaning**: Remove leading/trailing spaces from supplier names and standardize text.
  3. **Data Transformation**: Convert text columns to datetime objects and calculate shipping durations (Lead Time) in days.
  4. **Data Aggregation**: Group the data by supplier to calculate their average lead time.
  5. **Data Export**: Save the aggregated performance report as a clean CSV file for management.
