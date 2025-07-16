# 📊 Pandas Census Data Filtering Practice (July 16, 2025)

This document summarizes a practice session using Python and pandas to filter, sort, and inspect U.S. Census data from the [Census Bureau](https://www2.census.gov/programs-surveys/popest/datasets/2010-2020/state/totals/nst-est2020.csv). The work was done in VS Code and included reading, cleaning, filtering, and exporting data.

## 📚 Learning Context

This practice session was part of Day 4 exercises from the "Master Pandas for Data Manipulation - SQL to Python Translation" learning path, focusing on basic SELECT statements and WHERE clause filtering translated from SQL to pandas operations.
---

## ✅ Topics Covered

### 1. **Reading Census Data into Pandas**
```python
import pandas as pd
url = "https://www2.census.gov/programs-surveys/popest/datasets/2010-2020/state/totals/nst-est2020.csv"
population_df = pd.read_csv(url, encoding='latin1', skiprows=8)
```

### 2. **Cleaning Column Names**
```python
population_df.columns = population_df.columns.str.strip()
```

### 3. **Filtering by SUMLEV and REGION (State-Level, Region 3)**
```python
# Convert REGION to numeric in case of invalid values like 'X'
population_df['REGION'] = pd.to_numeric(population_df['REGION'], errors='coerce')
population_df = population_df.dropna(subset=['REGION'])
population_df['REGION'] = population_df['REGION'].astype(int)

# Filter for Region 3 states
filtered_df = population_df[
    (population_df['REGION'] == 3) & 
    (population_df['SUMLEV'] == 40)
]

# Display NAME and CENSUS2010POP
print(filtered_df[['REGION', 'NAME', 'CENSUS2010POP']].to_string(index=False))
```

### 4. **Checking for Invalid Data**
```python
# View unique values in REGION
print(population_df['REGION'].unique())

# Find non-numeric REGION entries
bad_rows = population_df[~population_df['REGION'].astype(str).str.isnumeric()]
print(bad_rows[['NAME', 'REGION']])
```

### 5. **Filtering by Population Range**
```python
# Filter for populations between 10,000 and 100,000
filtered_df = population_df[
    (population_df['CENSUS2010POP'] >= 10000) & 
    (population_df['CENSUS2010POP'] <= 100000)
]
print(filtered_df[['NAME', 'CENSUS2010POP']].to_string(index=False))
```

### 6. **Sorting by Population (Ascending)**
```python
sorted_df = filtered_df.sort_values(by='CENSUS2010POP', ascending=True)
print(sorted_df[['NAME', 'CENSUS2010POP']].to_string(index=False))
```

## 🗃️ Exporting to CSV
```python
sorted_df.to_csv("region3_small_states.csv", index=False)
```

## 🧠 Key Takeaways

- Use `skiprows` carefully to avoid skipping column headers
- Clean column names with `.str.strip()` to prevent subtle bugs
- Always wrap conditions in parentheses when using `&` or `|` in pandas filters
- Check for and handle invalid or non-numeric values using `pd.to_numeric(..., errors='coerce')`
- Use `.to_string(index=False)` for clean console output

## 📁 Files Used

- **Online Census CSV**: nst-est2020.csv (downloaded from Census Bureau)
- **Output**: region3_small_states.csv (exported filtered results)

## 🔗 Related Concepts

- SQL-style filtering in pandas
- Type coercion and NaN handling
- Sorting and subsetting large DataFrames
- Exporting filtered views to CSV
