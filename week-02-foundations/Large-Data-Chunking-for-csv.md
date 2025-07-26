# Chunking Approach for csv

The code demonstrates a pattern for handling large datasets while maintaining memory efficiency and providing progress visibility.

## File-based chunking
```python
for chunk in pd.read_csv('large_file.csv', chunksize=1000):
    process(chunk)

## Manual chunking with OFFSET/LIMIT
for offset in range(0, total_rows, chunk_size):
    query = f"SELECT * FROM table LIMIT {chunk_size} OFFSET {offset}"
    chunk = pd.read_sql(query, connection)
    process(chunk)
    ```