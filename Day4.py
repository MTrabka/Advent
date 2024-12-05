import requests
from dotenv import load_dotenv
import os

# Dataset
load_dotenv("config.env")
url = "https://adventofcode.com/2024/day/4/input"
session_cookie = os.getenv("SESSION")
headers = {
    "Cookie": f"session={session_cookie}"
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    input_data = response.text.strip()
else:
    print(f"Error: {response.status_code}")



grid = [line.strip() for line in input_data.split("\n") if line.strip()]
rows, cols = len(grid), len(grid[0])


target = "XMAS"

def check_diagonal(r, c, dr, dc, target, grid, rows, cols):
    for i in range(len(target)):
        nr, nc = r + dr * i, c + dc * i
        if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != target[i]:
            return False
    return True

found_positions = []
for r in range(rows):
    for c in range(cols):
        if check_diagonal(r, c, 1, 1, target, grid, rows, cols):  # down-right
            found_positions.append((r, c, "down-right"))
        if check_diagonal(r, c, 1, -1, target, grid, rows, cols):  # down-left
            found_positions.append((r, c, "down-left"))
        if check_diagonal(r, c, -1, 1, target, grid, rows, cols):  # up-right
            found_positions.append((r, c, "up-right"))
        if check_diagonal(r, c, -1, -1, target, grid, rows, cols):  # up-left
            found_positions.append((r, c, "up-left"))
        if check_diagonal(r, c, 1, 0, target, grid, rows, cols):  # top-to-bottom
            found_positions.append((r, c, "top-to-bottom"))
        if check_diagonal(r, c, -1, 0, target, grid, rows, cols):  # bottom-to-top
            found_positions.append((r, c, "bottom-to-top"))
        if check_diagonal(r, c, 0, 1, target, grid, rows, cols):  # left-to-right
            found_positions.append((r, c, "left-to-right"))
        if check_diagonal(r, c, 0, -1, target, grid, rows, cols):  # right-to-left
            found_positions.append((r, c, "right-to-left"))

print("Answer for part 1:", len(found_positions))

# Part 2
def find_xmas_patterns(grid, rows, cols):
    patterns = []
    for r in range(rows - 2):
        for c in range(cols - 2):
            if (
                grid[r][c] == "M"
                and grid[r][c+2] == "M"
                and grid[r+1][c+1] == "A"
                and grid[r+2][c] == "S"
                and grid[r+2][c+2] == "S"
            ):
                patterns.append((r+1, c+1))
            elif (
                grid[r][c] == "M"
                and grid[r][c+2] == "S"
                and grid[r+1][c+1] == "A"
                and grid[r+2][c] == "M"
                and grid[r+2][c+2] == "S"
            ):
                patterns.append((r+1, c+1))
            elif (
                grid[r][c] == "S"
                and grid[r][c+2] == "S"
                and grid[r+1][c+1] == "A"
                and grid[r+2][c] == "M"
                and grid[r+2][c+2] == "M"
            ):
                patterns.append((r+1, c+1))
            elif (
                grid[r][c] == "S"
                and grid[r][c+2] == "M"
                and grid[r+1][c+1] == "A"
                and grid[r+2][c] == "S"
                and grid[r+2][c+2] == "M"
            ):
                patterns.append((r+1, c+1))

    return patterns

xmas_patterns = find_xmas_patterns(grid, rows, cols)
print("Answer for part 2:", len(xmas_patterns))


