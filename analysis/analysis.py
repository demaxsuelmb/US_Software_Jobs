import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/demax.000/Documents/GitHub/US_Software_Jobs/data/raw/us-software-engineer-jobs-zenrows.csv')

df = pd.DataFrame(df)

# head
# print(df.head(4))

# columns
print(df.columns)

# describe
print(df.describe())

# size
print(df.len())


# print(df.head(4))
# print(df.head(4))
# print(df.head(4))


# print(df.head(4))
