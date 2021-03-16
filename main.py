from Node import Node
from BFS import BFS
from DFS import DFS
from AStar import AStar
from AStarNode import AStarNode
import pandas as pd

#tutaj trzeba wczytać plik , najlepiej chyba pandas
'''def readFile() :
    rows = pd.read_csv("Puzzles\puzzle", nrows = 1, header=None, delimiter=' ')[0]
    cols = pd.read_csv("Puzzles\puzzle", nrows=1, header=None, delimiter=' ')[1]
    array = [rows,cols]
    return array

array = readFile()
print(array)'''

order = 'DLUR'
puzzle = [[0,1,2,3],
                    [5,6,7,4],
                    [9,10,11,8],
                    [13,14,15,12]]
root = Node(puzzle, 0,'',4,4)


metric = 'Manhattan'

aStarRoot = AStarNode(puzzle,0,'',metric,4,4)
bfsPuzzleSolver = BFS()
dfsPuzzleSolver = DFS()
aStarPuzzleSolver = AStar()
bfsPuzzleSolver.solve(root,order)
#dfsPuzzleSolver.solve(root,order)
#aStarPuzzleSolver.solve(aStarRoot, metric)

