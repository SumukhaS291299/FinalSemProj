import os

import pandas as pd

# save a copy to a dataframe from github
df = pd.read_csv("https://raw.githubusercontent.com/SumukhaS291299/FinalSemProj/master/Details.csv")

# df.loc[df['column'] == row]  To get a perticular column with row

# sorted = df.sort_values("patientSSID")      If required sort dataframe

currlisID = []           # To create list of all patients
AllID = df["patientSSID"].tolist()          # List of all ids

for i in AllID:
    if i not in currlisID:
        currlisID.append(i)     #Append no dulpicate list of all Patients
print(currlisID)

for i in currlisID:
    NamesList = df.loc[df['patientSSID'] == i]
    print(NamesList)
    saveFIleName = "All_Details//" +str(i) +".csv"
    print(saveFIleName)
    NamesList.to_csv(saveFIleName)

directory ="All_Details"

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        df = pd.read_csv(f)
        listdf = df['Slno'].tolist()
        num = len(listdf)
        num = num-1
        most_recent = df.loc[df['Slno'] == listdf[num]]
        print(most_recent)
        RecFileName = "Updated_Details"+ f
        RecFileName = RecFileName.replace("All_Details","")
        print("File placed at => " + RecFileName)
        most_recent.to_csv(RecFileName)
