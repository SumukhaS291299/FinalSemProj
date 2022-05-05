import pandas as pd
import os
import sqlite3
directory ="Updated_Details"

conn=sqlite3.connect('Database//HighlyImportant.db')
C=conn.cursor()

# C.execute("CREATE TABLE AmbulanceDetails(slno int, patientSSID varchar(6) primary key, patientName varchar(50), doctorName varchar(50), val1 varchar(50), val2 varchar(50), lat varchar(50), longi varchar(50));")

list_val= []

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
       print(f)
       df = pd.read_csv(f)
       list_val = pd["patientSSID"].tolist()
       print(list_val)



       # conn.commit()
       # conn.close()
