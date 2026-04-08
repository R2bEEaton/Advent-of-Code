from helpers.matrix import Matrix, from_grid
import heapq
from PIL import Image
import colorsys

with open("code/maze.txt") as f:
    m = from_grid(f.read())

start = (1, 1)
q = []
visited = {}  # pos -> distance
heapq.heappush(q, (0, start))

while q:
    n, curr = heapq.heappop(q)
    if curr in visited:
        continue
    visited[curr] = n
    
    for npos, nval in m.neighbors(curr):
        if npos == (m.size[0] - 2, m.size[1] - 2):
            print(f"Distance to end: {n + 1}")
            visited[npos] = n + 1
            break
        if nval == " " and npos not in visited:
            heapq.heappush(q, (n + 1, npos))

# Create image from visited positions
max_dist = max(visited.values()) if visited else 1
img = Image.new('RGB', (m.size[1], m.size[0]), 'black')
pixels = img.load()

for pos, dist in visited.items():
    hue = (dist / max_dist)  # 0-1
    r, g, b = colorsys.hls_to_rgb(hue, 0.5, 1.0)
    pixels[pos[1], pos[0]] = (int(r * 255), int(g * 255), int(b * 255))

# img.show()
img.save("code/maze_solution_a.png")


# Shortest path is 353