import pandas as pd

df = pd.read_csv('C:/Users/demax.000/Documents/GitHub/US_Software_Jobs/data/raw/us-software-engineer-jobs-zenrows.csv')

df.to_excel('C:/Users/demax.000/Documents/GitHub/US_Software_Jobs/data/processed/us-software.xlsx', index=True)