import math
import re
from collections import defaultdict, deque
import requests
from dotenv import load_dotenv
import os

# Dataset
load_dotenv("config.env")
url = "https://adventofcode.com/2024/day/6/input"
session_cookie = os.getenv("SESSION")
headers = {
    "Cookie": f"session={session_cookie}"
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    input_data = response.text.strip()
else:
    print(f"Error: {response.status_code}")


def move_forward(direction, current_position):
    if direction == "left":
        return [current_position[0] - 1, current_position[1]]
    elif direction == "right":
        return [current_position[0] + 1, current_position[1]]
    elif direction == "up":
        return [current_position[0], current_position[1] - 1]
    elif direction == "down":
        return [current_position[0], current_position[1] + 1]
def turn(direction):
    if direction == "left":
        new_direction = "up"
    elif direction == "right":
        new_direction = "down"
    elif direction == "up":
        new_direction = "right"
    elif direction == "down":
        new_direction = "left"
    return new_direction
def starting_direction(map):
     for j in range(len(map)):
         for i in range(len(map[j])):
             if map[j][i]=="V"or map[j][i]=="v":
                 return [i,j],"down"
             elif map[j][i]=="^":
                 return [i,j],"up"
             elif map[j][i]=="<":
                 return [i,j],"left"
             elif map[j][i]==">":
                 return [i,j],"right"
def check_obstacle(map, current_position, direction):
    new_position = move_forward(direction, current_position)
    rows, cols = len(map), len(map[0])
    if not (0 <= new_position[1] < rows and 0 <= new_position[0] < cols):
        print("Finished")
        return current_position, direction, True,map
    if map[new_position[1]][new_position[0]] == "#":
        new_direction = turn(direction)
        return check_obstacle(map, current_position, new_direction)
    else:
        map[new_position[1]][new_position[0]] = "X"
        return new_position, direction, False,map

map_rows=input_data.split("\n")
map=[]
for row in map_rows:
    map.append(list(row))
curr_pos,starting_dir=starting_direction(map)

new_position, direction,flag,map = check_obstacle(map, curr_pos, starting_dir)
print(new_position)
print(direction)
positions=[[new_position]]
while not flag:
    new_position, direction,flag,map = check_obstacle(map, new_position, direction)
    positions.append(new_position)
    print(new_position)
    print(direction)

count = sum(row.count("X") for row in map)
print("Part 1 answer:", count + 1) #+1 because starting pos

#Part 2
