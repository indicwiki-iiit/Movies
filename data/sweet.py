# For generating SweetViz Report
import sweetviz as sv
import pandas as pd

df = pd.read_csv('FinalKB Telugu.csv')
report = sv.analyze(df)
report.show_html()