import os
import sqlite3
import pandas as pd
import sqlite3

conn = sqlite3.connect('Database//ImportantDeatils.db')

# Slno,patientSSID,patientName,doctorName,val1,val2,lati,longi
directory = "Updated_Details"
# conn.execute("CREATE TABLE All_Details (Slno varchar(10), patientSSID varchar(10) primary key ,patientName varchar(20),doctorName varchar(40),val1 varchar(100),val2 varchar(100) ,lati varchar(10),longi varchar(10)); ")

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        # print(f)
        df = pd.read_csv(f)

        sl = df["Slno"].tolist()
        Pssid = df["patientSSID"].tolist()
        Pname = df["patientName"].tolist()
        Dname = df["doctorName"].tolist()
        v1 = df["val1"].tolist()
        v2 = df["val1"].tolist()
        Lati = df["lati"].tolist()
        Longi = df["longi"].tolist()

        print(sl[0],Pssid[0],Pname[0],Dname[0],v1[0],v2[0],Lati[0],Longi[0])



# conn.commit()
# conn.close()

# conn.execute()