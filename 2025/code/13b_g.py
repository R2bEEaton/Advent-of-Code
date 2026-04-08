from helpers.matrix import Matrix, from_grid
import heapq
import random

with open("code/maze.txt") as f:
    m = from_grid(f.read())

start = (1, 1)
end = (m.size[0] - 2, m.size[1] - 2)
q = []
visited = {}  # pos -> distance
parent = {}  # pos -> previous position on shortest path
heapq.heappush(q, (0, start))
parent[start] = None

while q:
    n, curr = heapq.heappop(q)
    if curr in visited:
        continue
    visited[curr] = n
    
    for npos, nval in m.neighbors(curr):
        if npos == end:
            print(f"Distance to end: {n + 1}")
            visited[npos] = n + 1
            parent[npos] = curr
            break
        if nval == " " and npos not in visited:
            heapq.heappush(q, (n + 1, npos))
            if npos not in parent:
                parent[npos] = curr
        if nval == "X" and npos not in visited:
            heapq.heappush(q, (n + 5, npos))
            if npos not in parent:
                parent[npos] = curr
        if nval == "O" and npos not in visited:
            # Search row and column for another O
            for i in range(m.size[0]):
                if m.get((i, npos[1])) == "O" and (i, npos[1]) != npos:
                    heapq.heappush(q, (n + 1, (i, npos[1])))
                    if (i, npos[1]) not in parent:
                        parent[(i, npos[1])] = curr
                    break
            else:
                for i in range(m.size[1]):
                    if m.get((npos[0], i)) == "O" and (npos[0], i) != npos:
                        heapq.heappush(q, (n + 1, (npos[0], i)))
                        if (npos[0], i) not in parent:
                            parent[(npos[0], i)] = curr
                        break

# Reconstruct shortest path (as ordered list)
shortest_path_ordered = []
curr = end
while curr is not None:
    shortest_path_ordered.append(curr)
    curr = parent.get(curr)
shortest_path_ordered.reverse()  # Now goes from start to end

# Convert to set for easier lookup
shortest_path_set = set(shortest_path_ordered)

# Filter out X and O positions from the shortest path
valid_positions_on_path = [pos for pos in shortest_path_ordered if m[pos[0], pos[1]] == " "]

# Sample 14 random points for the code (on the shortest path)
code_positions = random.sample(valid_positions_on_path, 14)
# Sort them by their order in the path
code_positions.sort(key=lambda p: shortest_path_ordered.index(p))

# The code to place
code = "QMQZZQ6CTCTRAZ"

# Find all empty positions that are NOT on the shortest path
all_empty_positions = []
for r in range(m.size[0]):
    for c in range(m.size[1]):
        pos = (r, c)
        if m[r, c] == " " and pos not in shortest_path_set:
            all_empty_positions.append(pos)

print(f"Found {len(all_empty_positions)} empty positions NOT on shortest path")

# Pick 36 random points from positions NOT on the shortest path
random_positions = random.sample(all_empty_positions, 36)

# Characters to use (excluding X and O)
random_chars = "ABCDEFGHIJKLMNPQRSTUVWYZ0123456789"

# Create a copy of the maze to modify
modified_maze = Matrix(m.size, default=" ")
for r in range(m.size[0]):
    for c in range(m.size[1]):
        modified_maze[r, c] = m[r, c]

# Place the code (on the shortest path)
print("\nPlaced code characters (on shortest path):")
for i, pos in enumerate(code_positions):
    modified_maze[pos[0], pos[1]] = code[i]
    print(f"Placed '{code[i]}' at {pos}")

print("\nPlaced random characters (NOT on shortest path):")
# Place random characters (off the shortest path)
for pos in random_positions:
    char = random.choice(random_chars)
    modified_maze[pos[0], pos[1]] = char
    print(f"Placed '{char}' at {pos}")

# Save the modified maze
with open("code/maze_modified.txt", "w") as f:
    for r in range(modified_maze.size[0]):
        row = ""
        for c in range(modified_maze.size[1]):
            row += modified_maze[r, c]
        f.write(row + "\n")

print("\nModified maze saved to code/maze_modified.txt")