import os

import pandas as pd

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
