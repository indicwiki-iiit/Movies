import sweetviz as sv
import pandas as pd

df = pd.read_csv('Dataset8900 - FinalKB.csv')
report = sv.analyze(df)
report.show_html()