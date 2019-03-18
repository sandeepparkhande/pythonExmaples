import requests;
import pandas;
from pandas.io.json import json_normalize

url = "http://localhost:8081/message/allMessages";
response = requests.get(url)
print(" URL  ", url)
print(" Web Service Response ", response.text)
jsonResponse = response.json()

print(" Web Service Response ", jsonResponse)

df1 = json_normalize(jsonResponse)
df1.describe()

df2 = json_normalize(jsonResponse)
#df2.describe()

print(" SUM ", df1["id"].sum())
df3 = df1 + df2;

#print("SUM Dataframe ",df3)