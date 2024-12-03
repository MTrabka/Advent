import requests
from dotenv import load_dotenv
import os
import re


#Dataset
load_dotenv("config.env")
url = "https://adventofcode.com/2024/day/3/input"
session_cookie = os.getenv("SESSION")
headers = {
    "Cookie": f"session={session_cookie}"
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    input_data = response.text
    #print("Input data:")
    #print(type(input_data))
else:
    print(f"Error: {response.status_code}")

def find_sequence(input):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches=re.findall(pattern, input)
    return matches

def multiply_list_of_tuples(list_of_tuples):
    result=0
    for item in list_of_tuples:
        result += int(item[0]) * int(item[1])
    return result

found=find_sequence(input_data)
outcome=multiply_list_of_tuples(found)


# Part 2

def find_patterns(text):
    patterns = [r"do\(\)", r"don't\(\)", r"mul\(\d{1,3},\d{1,3}\)"]
    matches = []
    for pattern in patterns:
        matches.extend(re.finditer(pattern, text))
    matches_sorted = sorted(matches, key=lambda m: m.start())
    return [match.group() for match in matches_sorted]

def extract_valid_elements(matches):
    valid = []
    capturing = False
    for item in matches:
        if item == "do()":
            capturing = True
        elif item == "don't()":
            capturing = False
        elif capturing:
            valid.append(item)
    return valid

def extract_numbers_as_tuples(valid_elements):
    number_tuples = []
    for element in valid_elements:
        match = re.search(r"mul\((\d+),(\d+)\)", element)
        if match:
            number_tuples.append((int(match.group(1)), int(match.group(2))))
    return number_tuples

outcome2=find_patterns(input_data)
valid_first=[]
valid=[]
for item in outcome2:
    if item != "do()":
        valid_first.append(item)
    else:
        break


valid_elements = extract_valid_elements(outcome2)
valid_all=(valid_first+valid_elements)
new_data=extract_numbers_as_tuples(valid_all)
result2=multiply_list_of_tuples(new_data)
print(result2)