# Project 08: 📊 Data Analysis with Pandas

> **Analyze real datasets with NumPy and Pandas**

## 🎯 Real-World Data Science

- NumPy arrays and operations
- Pandas DataFrames
- Reading CSV files
- Data cleaning and transformation
- Grouping and aggregation
- Basic statistics

## 📚 Example

```python
import pandas as pd

df = pd.read_csv('data.csv')
summary = df.groupby('category')['sales'].sum()
```

## 🏃 Run

```bash
python main.py && pytest test_solution.py -v
```

**Status:** ✅ Complete!
