import pandas as pd

df = pd.read_csv("data/Dataset8900 - FinalKB.csv")
df.fillna("NaN")
df.to_pickle("./123.pkl")

