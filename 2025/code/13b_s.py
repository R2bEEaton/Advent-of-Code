from helpers.matrix import Matrix, from_grid
import heapq
from PIL import Image
import colorsys

with open("code/maze_modified.txt") as f:
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
        if nval in " ABCDEFGHIJKLMNPQRSTUVWYZ0123456789" and npos not in visited:
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

# Extract letters and numbers from the path, and count Xs and Os
letters_and_numbers = []
x_count = 0
o_count = 0

for pos in shortest_path_ordered:
    char = m[pos[0], pos[1]]
    if char == "X":
        x_count += 1
    elif char == "O":
        o_count += 1
    elif char not in " #":  # Not a space or wall
        letters_and_numbers.append(char)

print("\nLetters and numbers on shortest path:")
print("".join(letters_and_numbers))
assert "".join(letters_and_numbers) == "QMQZZQ6CTCTRAZ"
print(f"\nXs on optimal path: {x_count}")
print(f"Os on optimal path: {o_count}")

# Convert to set for visualization
shortest_path_set = set(shortest_path_ordered)

# Create image from visited positions
max_dist = max(visited.values()) if visited else 1
img = Image.new('RGB', (m.size[1], m.size[0]), 'black')
pixels = img.load()

# First, color all visited positions
for pos, dist in visited.items():
    if pos in shortest_path_set:
        pixels[pos[1], pos[0]] = (255, 0, 0)  # Red for shortest path
    elif m[pos[0], pos[1]] == "O":
        pixels[pos[1], pos[0]] = (255, 255, 255)
    elif m[pos[0], pos[1]] == "X":
        pixels[pos[1], pos[0]] = (128, 128, 128)
    else:
        hue = (dist / max_dist)  # 0-1
        r, g, b = colorsys.hls_to_rgb(hue, 0.5, 1.0)
        pixels[pos[1], pos[0]] = (int(r * 255), int(g * 255), int(b * 255))

# Then, add all X and O positions that weren't visited
for r in range(m.size[0]):
    for c in range(m.size[1]):
        if (r, c) not in visited:
            if m[r, c] == "O":
                pixels[c, r] = (255, 255, 255)
            elif m[r, c] == "X":
                pixels[c, r] = (128, 128, 128)

img.save("code/maze_solution_b.png")
print("\nVisualization saved to code/maze_solution_b.png")