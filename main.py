from Node import Node
from BFS import BFS
from DFS import DFS
from AStar import AStar
from AStarNode import AStarNode
import pandas as pd
import time

#tutaj trzeba wczytać plik , najlepiej chyba pandas
def readFile() :
    dimensions = pd.read_csv("Puzzles/puzzle", nrows = 1, header=None, delimiter=' ')
    rows = pd.read_csv("Puzzles/puzzle", skiprows = [0], header=None, delimiter=' ')
    array = rows.values.tolist()
    r = dimensions[0].values[0]
    c = dimensions[1].values[0]
    return [array,c,r]


data = readFile()
array = data[0]
cols = data[1]
rows = data[2]

puzzle = array
order = 'URDL'

metric = 'Manhattan'
root = Node(puzzle, 0,'',cols,rows)
aStarRoot = AStarNode(puzzle,0,'',metric,cols,rows)
bfsPuzzleSolver = BFS()
dfsPuzzleSolver = DFS()
aStarPuzzleSolver = AStar()

start = time.time()

bfsPuzzleSolver.solve(root,order)
#dfsPuzzleSolver.solve(root,order)
#aStarPuzzleSolver.solve(aStarRoot, metric)

end = time.time()
print('Czas to: ', end - start)

