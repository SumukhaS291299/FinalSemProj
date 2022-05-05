import os
import sqlite3
import pandas as pd
import sqlite3

conn = sqlite3.connect('Database//ImportantDeatils.db')

cur = conn.cursor()

# Slno,patientSSID,patientName,doctorName,val1,val2,lati,longi
directory = "Updated_Details"
# conn.execute("CREATE TABLE All_Details (Slno varchar(10), patientSSID varchar(10) primary key ,patientName varchar(20),doctorName varchar(40),val1 varchar(100),val2 varchar(100) ,lati varchar(10),longi varchar(10)); ")

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print("Working on file "+str(f))
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

        str_update = r"INSERT INTO All_Details (Slno,patientSSID,patientName,doctorName,val1,val2,lati,longi) VALUES ("+str(sl[0])+","+str(Pssid[0])+","+str(Pname[0])+","+str(Dname[0])+","+str(v1[0])+","+str(v2[0])+","+str(Lati[0])+","+str(Longi[0])+");"

        print(str_update)

        # params =(Slno,patientSSID,patientName,doctorName,val1,val2,lati,longi)

        cur.execute(str_update)
        conn.commit()
        # conn.close()
print(cur.fetchall())
conn.close()
# All are string convertd


# conn.execute()