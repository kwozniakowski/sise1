from Node import Node
from BFS import BFS
from DFS import DFS
from AStar import AStar
from AStarNode import AStarNode
puzzle = [[1,2,3,7],
                    [8,4,5,6],
                    [9,10,11,15],
                    [0,12,13,14]]
root = Node(puzzle, 0,'')
aStarRoot = AStarNode(puzzle,0,'')
bfsPuzzleSolver = BFS()
dfsPuzzleSolver = DFS()
aStarPuzzleSolver = AStar()
#bfsPuzzleSolver.solve(root)
dfsPuzzleSolver.solve(root)
#aStarPuzzleSolver.solve(aStarRoot)

