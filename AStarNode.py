import copy
import math


class AStarNode :
    def __init__(self,puzzle,depth,solution):
        self.cols = 4
        self.rows = 4
        self.puzzle = puzzle
        for i in range(0, len(puzzle) ):
            for j in range(0,len(puzzle[i]) ):
                if puzzle[i][j] == 0 :
                    self.XZero = j
                    self.YZero = i
        self.depth = depth
        self.solution = solution
        self.manhattanDistance = self.manhattanDistance()
        if len(solution) == 0:
            self.previousOperator = None
        else:
            self.previousOperator = solution[-1]

    def isSolved(self):
        solved = True
        n = self.puzzle[0][0]
        for row in self.puzzle :
            for number in row :
                if not number >= n:
                    solved = False
                n = number
        return solved


    def moveLeft(self):
        newPuzzle = copy.deepcopy(self.puzzle)
        buffer = newPuzzle[self.YZero][self.XZero-1]
        newPuzzle[self.YZero][self.XZero - 1] = 0
        newPuzzle[self.YZero][self.XZero] = buffer
        newNode = AStarNode(newPuzzle,self.depth + 1, self.solution + 'L')
        return newNode

    def moveRight(self):
            newPuzzle = copy.deepcopy(self.puzzle)
            buffer = newPuzzle[self.YZero][self.XZero+1]
            newPuzzle[self.YZero][self.XZero + 1] = 0
            newPuzzle[self.YZero][self.XZero] = buffer
            newNode = AStarNode(newPuzzle,self.depth + 1,self.solution + 'R')
            return newNode

    def moveUp(self):
            newPuzzle = copy.deepcopy(self.puzzle)
            buffer = newPuzzle[self.YZero-1][self.XZero]
            newPuzzle[self.YZero-1][self.XZero] = 0
            newPuzzle[self.YZero][self.XZero] = buffer
            newNode = AStarNode(newPuzzle,self.depth + 1,self.solution + 'U')
            return newNode

    def moveDown(self):
            newPuzzle = copy.deepcopy(self.puzzle)
            buffer = newPuzzle[self.YZero+1][self.XZero]
            newPuzzle[self.YZero+1][self.XZero] = 0
            newPuzzle[self.YZero][self.XZero] = buffer
            newNode = AStarNode(newPuzzle,self.depth + 1,self.solution + 'D')
            return newNode

    def canMoveLeft(self):
        if self.XZero != 0 and self.previousOperator != 'R':
            return True
        else :
            return False
    def canMoveRight(self):
        if self.XZero < self.cols - 1 and self.previousOperator != 'L':
            return True
        else :
            return False
    def canMoveUp(self):
        if self.YZero != 0 and self.previousOperator != 'D':
            return True
        else :
            return False
    def canMoveDown(self):
        if self.YZero < self.rows-1 and self.previousOperator != 'U':
            return True
        else :
            return False

    def manhattanDistance(self):
        distance = 0
        for i in range (0,self.rows) :
            for j in range (0, self.cols) :
                number = self.puzzle[i][j]
                vertical = math.floor( number / self.cols )
                horizontal = number % self.cols
                distance = distance + abs(i-vertical) + abs(j-horizontal)
        return distance
