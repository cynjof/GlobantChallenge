
# Data Processing Pipeline

## Overview

This document outlines the steps involved in a data processing pipeline that takes CSV data, performs a transformation, and inserts the processed data into a MySQL database via an API.

## Process Steps

### 1. Data Ingestion

- Input: CSV file containing raw data.
- Output: Raw data is loaded into memory.

### 2. Data Transformation

- Transformation: Apply necessary data transformations (data cleaning, formatting).
- Output: List of dictionaries.

### 3. API Call

- Input: List.
- Action: Call an API to insert the data into a MySQL database.
- Output: Confirmation of successful API call.
