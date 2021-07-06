import pandas as pd

file_tobe_analysed = pd.read_csv("Dataset8900 - FinalKB.csv")

count = [0] * 8929

# Function to generate Boolean values based on availability of value in the cell
def analyse(): 
    for i in range(len(file_tobe_analysed)):
        # print(i)
        for j in range(len(file_tobe_analysed.columns)):
            # print(j)
            if file_tobe_analysed.isna().iloc[i][j]:
                count[i] += 1

def make_emptyfile():
    df = file_tobe_analysed.isna()
    df.to_csv("emptyvalues.csv")

make_emptyfile()
# analyse()
print(count)
