import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/SumukhaS291299/FinalSemProj/master/Details.csv")

print(df)

NamesList=df.loc[df['patientName'] == 'A']



print(NamesList)