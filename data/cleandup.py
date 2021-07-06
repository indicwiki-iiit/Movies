import pandas as pd

# Drops Duplicates
df = pd.read_csv('data/images data - Sheet2.csv')
df.drop_duplicates(subset='IMDbID',inplace=True)
df.to_csv('1.csv')