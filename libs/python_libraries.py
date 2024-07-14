## Asyncio

import asyncio

async def fetch_data(url):
    print(f"Fetching {url}")
    await asyncio.sleep(1)
    return f"Data from {url}"

async def main():
    url = ["https://jsonplaceholder.typicode.com/todos/1", "https://jsonplaceholder.typicode.com/todos/2"]
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)
    print(results)

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

