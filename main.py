"""Importing module pandas for my function."""
import polars as pl
df = pl.read_csv("iris.csv")
print(df)

def avg_88(data):
    """"This is a mean function."""
    result = data.mean()
    return result

print(avg_88(df.select('sepal.length')))