import pandas as pd

df1 = pd.read_csv('FinalKB Telugu.csv')
df2 = pd.read_csv('transliterated_extra.csv')

# Merge two different csv files
df = pd.merge(df1,df2,on='IMDbID',how='outer')

df.to_csv('extranew.csv')