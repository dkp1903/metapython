## Asyncio

import asyncio

async def fetch_financial_data(row):
    # Simulate an I/O-bound operation
    await asyncio.sleep(1)
    return row

async def process_financial_data(row):
    # Simulate processing the data
    await asyncio.sleep(1)
    processed_data = {**row, 'processed': True}
    return processed_data

async def main():
    tasks = []
    for _, row in df.iterrows():
        fetch_task = fetch_financial_data(row)
        tasks.append(fetch_task)
    
    # Fetch all data concurrently
    fetched_data = await asyncio.gather(*tasks)
    
    tasks = []
    for data in fetched_data:
        process_task = process_financial_data(data)
        tasks.append(process_task)
    
    # Process all data concurrently
    processed_data = await asyncio.gather(*tasks)
    
    print("Processed Data:")
    for data in processed_data:
        print(data)

# Run the asyncio event loop
asyncio.run(main())



## Pandas/Np

# Merge two DataFrames on a common column 'barsId'
df1 = pd.read_csv('financial_info.csv')
df2 = pd.read_csv('financial_ratings.csv')

merged_df = pd.merge(df1, df2, on='barsId')

print(merged_df)

# Use NumPy's where function to create a new column 'investment_grade'
df['investment_grade'] = np.where(df['fitchRating'] >= 'BBB', 'Yes', 'No')

print(df)

## SQLite

# Query all data
cursor.execute('SELECT * FROM financial_data')
rows = cursor.fetchall()

print("All Data:")
for row in rows:
    print(row)

# Filter data where fitchRating is greater than 'BBB'
cursor.execute('SELECT * FROM financial_data WHERE fitchRating > ?', ('BBB',))
filtered_rows = cursor.fetchall()

print("\nFiltered Data (fitchRating > 'BBB'):")
for row in filtered_rows:
    print(row)

