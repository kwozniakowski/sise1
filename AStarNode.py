import copy
import math


class AStarNode :
    def __init__(self,puzzle,depth,solution,metric,cols,rows):
        self.cols = cols
        self.rows = rows
        self.puzzle = puzzle
        for i in range(0, len(puzzle) ):
            for j in range(0,len(puzzle[i]) ):
                if puzzle[i][j] == 0 :
                    self.XZero = j
                    self.YZero = i
        self.depth = depth
        self.solution = solution
        self.metric = metric

        if(metric == 'Hamming'):
            self.totalDistance = self.hammingDistance() + self.depth
        else:
            self.totalDistance = self.manhattanDistance() + self.depth

        if len(solution) == 0:
            self.previousOperator = None
        else:
            self.previousOperator = solution[-1]

    def isSolved(self):
        solved = True
        previous = self.puzzle[0][0]
        for i in range(0,self.rows):
            for j in range(0,self.cols):
                element = self.puzzle[i][j]
                if (i+1) * (j+1) == self.cols * self.rows:
                    if element != 0 :
                        solved = False
                else:
                    if not element >= previous:
                        solved = False
                previous = element
        return solved


    def moveLeft(self):
        newPuzzle = copy.deepcopy(self.puzzle)
        buffer = newPuzzle[self.YZero][self.XZero-1]
        newPuzzle[self.YZero][self.XZero - 1] = 0
        newPuzzle[self.YZero][self.XZero] = buffer
        newNode = AStarNode(newPuzzle,self.depth + 1, self.solution + 'L', self.metric,self.cols,self.rows)
        return newNode

    def moveRight(self):
            newPuzzle = copy.deepcopy(self.puzzle)
            buffer = newPuzzle[self.YZero][self.XZero+1]
            newPuzzle[self.YZero][self.XZero + 1] = 0
            newPuzzle[self.YZero][self.XZero] = buffer
            newNode = AStarNode(newPuzzle,self.depth + 1,self.solution + 'R',self.metric,self.cols,self.rows)
            return newNode

    def moveUp(self):
            newPuzzle = copy.deepcopy(self.puzzle)
            buffer = newPuzzle[self.YZero-1][self.XZero]
            newPuzzle[self.YZero-1][self.XZero] = 0
            newPuzzle[self.YZero][self.XZero] = buffer
            newNode = AStarNode(newPuzzle,self.depth + 1,self.solution + 'U',self.metric,self.cols,self.rows)
            return newNode

    def moveDown(self):
            newPuzzle = copy.deepcopy(self.puzzle)
            buffer = newPuzzle[self.YZero+1][self.XZero]
            newPuzzle[self.YZero+1][self.XZero] = 0
            newPuzzle[self.YZero][self.XZero] = buffer
            newNode = AStarNode(newPuzzle,self.depth + 1,self.solution + 'D',self.metric,self.cols,self.rows)
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
                if number != 0 :
                    vertical = math.floor( number / self.cols )
                    horizontal = number % self.cols
                    distance = distance + abs(i-vertical) + abs(j-horizontal)
        return distance

    def hammingDistance(self):
        distance = 0
        for i in range (0,self.rows) :
            for j in range (0, self.cols) :
                number = self.puzzle[i][j]
                if number != 0:
                    if number != i * self.cols + j :
                        distance = distance + 1
        return distance