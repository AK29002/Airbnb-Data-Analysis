import pandas as pd

df = pd.read_csv('C:\\Users\\Arnav Kuchhal\\OneDrive\\Desktop\\Arnav\\College\\Airbnb Project\\Airbnb Data.csv', parse_dates=['date'])

print("Shape of dataset:", df.shape)
print("\nColumn names:", df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values per column:")
print(df.isna().sum())

print("\nSummary statistics:")
print(df.describe(include='all').T.head(10))