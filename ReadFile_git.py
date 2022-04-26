import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/SumukhaS291299/FinalSemProj/main/DronePPM.csv")

print(df)

print(df['Aux4'].tolist())