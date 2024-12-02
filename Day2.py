import numpy as np
import pandas as pd
import requests
from dotenv import load_dotenv
import os


#Dataset
load_dotenv("config.env")
url = "https://adventofcode.com/2024/day/2/input"
session_cookie = os.getenv("SESSION")
headers = {
    "Cookie": f"session={session_cookie}"
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    input_data = response.text
    #print("Input data:")
    #print(input_data)
else:
    print(f"Error: {response.status_code}")

def dataConversion(input_data): #To list of lists of int
    data_input=input_data.split("\n")
    data = []
    for line in data_input:
        input_line = line.split(" ")
        data.append(input_line)
    data.pop()
    data_int = [[int(x) for x in inner_list] for inner_list in data]
    return data_int

data_int=dataConversion(input_data)
def is_no_grater_than3(data):
    isLineSafe=[]
    for line in data:
        line_safe = 0
        for j in range(len(line) - 1):
            if line[j] == line[j + 1]:
                line_safe += 1
            elif abs(line[j] - line[j + 1]) > 3:
                line_safe += 1
        isLineSafe.append(line_safe)
    return isLineSafe

def is_monotonic(item):
    return all(item[i] < item[i + 1] for i in range(len(item) - 1)) or \
           all(item[i] > item[i + 1] for i in range(len(item) - 1))

isLineSafe=is_no_grater_than3(data_int)
unsafe=[]
potentialSafe=[]
for j in range(len(isLineSafe)):
    if isLineSafe[j] == 0:
        potentialSafe.append(data_int[j])
    else:
        unsafe.append(data_int[j])

Safe=[]
for item in potentialSafe:
    if is_monotonic(item):
        Safe.append(item)
    else:
        unsafe.append(item)

# Part 2
safe_count=len(Safe)


def is_valid(item):

    if not is_monotonic(item):
        return False

    for j in range(len(item) - 1):
        if abs(item[j] - item[j + 1]) > 3:
            return False
    return True


safe_after_removal = []
still_unsafe = []

for item in unsafe:
    modified = False
    for i in range(len(item)):

        modified_item = item[:i] + item[i + 1:]

        if is_valid(modified_item):
            safe_after_removal.append(modified_item)
            modified = True
            break
    if not modified:
        still_unsafe.append(item)

safe_count+=len(safe_after_removal)
print(safe_count)