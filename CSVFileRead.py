import pandas as pd;
import numpy as nm;
import csv;


##Dictionary Data

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }


# Read CSV FILE
amzn = pd.read_csv("D:\Sandeep\AMZN.csv")
print("Open Column sum is ",amzn["Open"].sum()/amzn["High"].sum())

## Dataframe from Dictionary
dictData = pd.DataFrame(dict)

print(dictData.sort_values("area").sort_values("population"))

def readWriteCsv():
    f = open("D:\Sandeep\AMZNNew.csv", "w")

    with open("D:\Sandeep\AMZN.csv") as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            print(row[0], row[1])
            f.write(row[0] + "," + row[1] + "\n")

    f.close()
    # print(brics.sort_values("Date"));
