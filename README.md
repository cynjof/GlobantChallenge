# GlobantChallenge

# Data Processing Pipeline

## Overview

This document outlines the steps involved in a data processing pipeline that takes CSV data, performs a transformation, and inserts the processed data into a MySQL database via an API.

## Process Steps

### 1. Data Ingestion

- Input: CSV file containing raw data.
- Output: Dataframe with the data.

### 2. Data Transformation

- Apply necessary data transformations (data cleaning, formatting).
- Parse data into a list of dictionaries

### 3. API Call

- Input: list of dictionaries
- Action: Call an API to insert the data into a MySQL database.
- Output: Confirmation of successful API call.