from mazelib import Maze
from mazelib.generate.Kruskal import Kruskal

m = Maze()
m.generator = Kruskal(50, 50)
m.generate()

print(m)

