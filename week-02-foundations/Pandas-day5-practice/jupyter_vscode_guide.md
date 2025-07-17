# Getting Started with Jupyter in VS Code

*A beginner-friendly guide to setting up and using Jupyter notebooks in VS Code for data analysis and SQL-to-pandas conversion*

## Why Use Jupyter in VS Code?

Jupyter notebooks in VS Code combine the best of both worlds:
- **Familiar VS Code interface** with all your favorite extensions
- **Interactive data exploration** with immediate visual feedback
- **Perfect for iterative development** - especially useful for converting SQL queries to pandas
- **Built-in debugging and IntelliSense** for better code quality

## Prerequisites

- VS Code installed
- Python installed on your system
- Basic familiarity with VS Code

## Setup Steps

### 1. Install Required Extensions

Open VS Code and install the **Python extension** by Microsoft:
- Go to Extensions (`Ctrl+Shift+X`)
- Search for "Python" 
- Install the official Microsoft Python extension
- This automatically includes Jupyter support

### 2. Set Up Your Python Environment

#### Option A: Use a Virtual Environment (Recommended)
```bash
# Navigate to your project folder
cd your-project-folder

# Create virtual environment
python -m venv .venv

# Activate it
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# Install required packages
pip install pandas jupyter ipykernel matplotlib seaborn
```

#### Option B: Use Global Python
```bash
pip install pandas jupyter ipykernel matplotlib seaborn
```

### 3. Create Your First Notebook

1. In VS Code, create a new file with `.ipynb` extension (e.g., `data_analysis.ipynb`)
2. VS Code will automatically recognize it as a Jupyter notebook
3. Click "Select Kernel" in the top-right corner
4. Choose your Python interpreter (the one where you installed the packages)

## Essential First Cell Setup

Start every notebook with this setup cell:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configure pandas display options for better visualization
pd.set_option('display.max_columns', None)    # Show all columns
pd.set_option('display.width', None)          # Don't wrap output
pd.set_option('display.max_colwidth', 100)    # Limit column width
pd.set_option('display.max_rows', 20)         # Limit rows shown

# Configure matplotlib for inline plots
%matplotlib inline

print("Setup complete! 🚀")
```

## Key Shortcuts You Need to Know

### Running Cells
- `Shift+Enter`: Run current cell and move to next
- `Ctrl+Enter`: Run current cell and stay on it
- `Alt+Enter`: Run current cell and create new cell below

### Cell Management
- `A`: Add cell above
- `B`: Add cell below
- `DD`: Delete cell (press D twice)
- `M`: Convert to markdown cell
- `Y`: Convert to code cell
- `Z`: Undo cell deletion

### Navigation
- `Up/Down arrows`: Navigate between cells
- `Enter`: Enter edit mode
- `Esc`: Exit edit mode

## Practical Workflow for Data Analysis

### Structure Your Notebook Like This:

#### Cell 1: Setup and Imports
```python
# Always start with your imports and configuration
import pandas as pd
import numpy as np
# ... your setup code from above
```

#### Cell 2: Data Loading
```python
# Load your data
df = pd.read_csv('your_data.csv')

# Quick data overview
print(f"Dataset shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
df.head()
```

#### Cell 3: Data Exploration
```python
# Understand your data
df.info()
df.describe()
df.nunique()
```

#### Cell 4: Data Analysis (SQL to Pandas Example)
```python
# Original SQL (as comment):
# SELECT column1, COUNT(*) as count
# FROM table
# WHERE condition = 'value'
# GROUP BY column1
# ORDER BY count DESC

# Pandas equivalent:
result = (df[df['condition'] == 'value']
          .groupby('column1')
          .size()
          .reset_index(name='count')
          .sort_values('count', ascending=False))

result.head(10)
```

#### Cell 5: Visualization
```python
# Quick visualization
result.plot(kind='bar', x='column1', y='count')
plt.title('Your Chart Title')
plt.show()
```

## Pro Tips for Better Jupyter Experience

### 1. Use Markdown Cells for Documentation
Create markdown cells to document your analysis:
```markdown
## Data Analysis Section
This section explores the relationship between...

### Key Findings:
- Finding 1
- Finding 2
```

### 2. Leverage VS Code Features
- **Variable Explorer**: Use the Jupyter Variables panel to see all your DataFrames
- **IntelliSense**: Get autocomplete for pandas methods
- **Debugging**: Set breakpoints in your notebook cells
- **Git Integration**: Track changes to your notebooks

### 3. Quick Data Inspection Commands
```python
# Quick ways to inspect your data
df.shape                    # Dimensions
df.columns.tolist()        # Column names as list
df.dtypes                  # Data types
df.memory_usage()          # Memory usage
df.sample(5)               # Random sample
```

### 4. Performance Monitoring
```python
# Time your operations
%%time
# Your code here

# Memory usage
df.memory_usage(deep=True).sum()
```

## Common Issues and Solutions

### Issue: "ipykernel not found"
**Solution:**
```bash
pip install ipykernel
```

### Issue: Pandas import error
**Solution:**
1. Check your Python interpreter (`Ctrl+Shift+P` → "Python: Select Interpreter")
2. Install pandas in the correct environment: `pip install pandas`

### Issue: Plots not showing
**Solution:**
Add `%matplotlib inline` to your setup cell

### Issue: Kernel won't start
**Solution:**
1. Restart VS Code
2. Try "Restart Kernel" from the command palette
3. Reinstall ipykernel: `pip install ipykernel --force-reinstall`

## Best Practices

1. **Keep cells focused**: One concept per cell
2. **Use meaningful variable names**: `sales_df` instead of `df`
3. **Comment your SQL conversions**: Always include the original SQL as a comment
4. **Save frequently**: Notebooks can lose unsaved work
5. **Use version control**: Commit your `.ipynb` files to git
6. **Clear outputs before committing**: Keep your repository clean

## Next Steps

Once you're comfortable with the basics:
- Explore pandas plotting capabilities
- Learn about interactive widgets with `ipywidgets`
- Try advanced pandas operations (pivot tables, window functions)
- Experiment with data visualization libraries like Plotly

## Resources

- [VS Code Jupyter Documentation](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Jupyter Notebook Tips](https://jupyter-notebook.readthedocs.io/en/stable/)

---

*Happy coding! 🐍📊*