import numpy as np
import pandas as pd
import requests
from dotenv import load_dotenv
import os
load_dotenv("config.env")
#Dataset
url = "https://adventofcode.com/2024/day/1/input"
session_cookie = os.getenv("SESSION")
headers = {
    "Cookie": f"session={session_cookie}"
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    input_data = response.text
    print("Input data:")
    print(input_data)
else:
    print(f"Error: {response.status_code}")


#Converting the data
input_data_splited = input_data.split("\n")
new_data=[]
for line in input_data_splited:
    new_data.append(line.split("   "))

ListaA=[]
ListaB=[]

for item in new_data[:len(new_data)-1]:
    ListaA.append(item[0])
    ListaB.append(item[1])

ListaA_int=[]
ListaB_int=[]
for item in ListaA:
    ListaA_int.append(int(item))
for item in ListaB:
    ListaB_int.append(int(item))


ListaA_int.sort()
ListaB_int.sort()
distance=[]
for i in range(len(ListaA_int)):
    distance.append(abs(ListaA_int[i]-ListaB_int[i]))

result=sum(distance)
print(result)

### Part 2
repetitive=[]
for i in range(len(ListaA_int)):
    count=0
    for j in range(len(ListaA_int)):
        if ListaA_int[i]==ListaB_int[j]:
            count+=1
    repetitive.append(count)
similarities=[]
for i in range(len(ListaA_int)):
    similarities.append(ListaA_int[i]*repetitive[i])

result2=sum(similarities)
print(result2)
