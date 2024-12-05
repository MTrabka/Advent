import math
import re
from collections import defaultdict, deque
import requests
from dotenv import load_dotenv
import os

# Dataset
load_dotenv("config.env")
url = "https://adventofcode.com/2024/day/5/input"
session_cookie = os.getenv("SESSION")
headers = {
    "Cookie": f"session={session_cookie}"
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    input_data = response.text.strip()
else:
    print(f"Error: {response.status_code}")

data=input_data.split("\n")
rules=[]
update_list=[]
pattern=r"\d{2}\|\d{2}"
for line in data:
    if re.match(pattern, line):
        rules.append(line)
    else:
        update_list.append(line)

update_list = [line for line in update_list if line.strip()]

rules_clean=[]
for line in rules:
    rules_clean.append(list(map(int, line.split("|"))))

update_list_clean=[]
for line in update_list:
    update_list_clean.append(list(map(int, line.split(","))))

item_matches = {}
for item_index, item in enumerate(update_list_clean):
    item_set = set(item)
    matching_rules = []

    for rule_index, rule in enumerate(rules_clean):
        rule_set = set(rule)
        if rule_set.issubset(item_set):
            matching_rules.append(rule_index)

    item_matches[tuple(item)] = matching_rules

good_update_list = []
for item in update_list_clean:
    good_item = []
    item_set = set(item)
    for rule_index in item_matches[tuple(item)]:
        rule = rules_clean[rule_index]
        if set(rule).issubset(item_set):
            good_rule = []
            for i in range(len(item)):
                if item[i] == rule[0]:
                    for j in range(i + 1, len(item)):
                        if item[j] == rule[1]:
                            good_rule.append(1)
                        else:
                            good_rule.append(0)
            if 1 in good_rule:
                good_item.append(1)
            else:
                good_item.append(0)
    if 0 in good_item:
        good_update_list.append(0)
    else:
        good_update_list.append(1)

#print(good_update_list)
#print(len(good_update_list))
#print(len(item_matches))


printable = []

for i in range(len(good_update_list)):
    if good_update_list[i] == 1:
        printable.append(update_list_clean[i])

#print(printable)
middles=[]
for item in printable:
    mid=len(item)//2
    middles.append(item[mid])
print("Part 1 answer: ",sum(middles))

#Part 2
unprintable=[]
for i in range(len(good_update_list)):
    if good_update_list[i] == 0:
        unprintable.append(update_list_clean[i])
rules_for_unprintable=[]
for item in unprintable:
    rules_for_unprintable.append(item_matches[tuple(item)])
rules_for_unprintable_full=[]
for item in rules_for_unprintable:
    rules_for_unprintable_item=[]
    for i in range(len(item)):
        rules_for_unprintable_item.append(rules_clean[item[i]])
    rules_for_unprintable_full.append(rules_for_unprintable_item)

#
def topological_sort(data, rules):
    adj_list = defaultdict(list)
    in_degree = defaultdict(int)

    # Initialize the in-degree of all nodes to 0
    for number in data:
        in_degree[number] = 0

    # Build the graph and update in-degrees
    for rule in rules:
        u, v = rule
        adj_list[u].append(v)
        in_degree[v] += 1

    # Queue for nodes with in-degree 0 (no dependencies)
    queue = deque([node for node in data if in_degree[node] == 0])

    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        # Decrease the in-degree of the neighbors
        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(data):
        return "Cycle detected, no valid ordering"
    return result

sorted_data=[]
for i in range(len(unprintable)):
    sorted_data.append(topological_sort(unprintable[i], rules_for_unprintable_full[i]))


middles2=[]
for item in sorted_data:
    mid=math.floor(len(item)//2)
    middles2.append(item[mid])
print("Part 2 answer: ",sum(middles2))
# Output the reordered updates
