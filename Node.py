import copy


class Node:
    def __init__(self, puzzle, depth, solution, cols, rows):
        self.cols = cols
        self.rows = rows
        self.puzzle = puzzle
        for i in range(0, len(puzzle)):
            for j in range(0, len(puzzle[i])):
                if puzzle[i][j] == 0:
                    self.XZero = j
                    self.YZero = i
        self.depth = depth
        self.solution = solution
        if len(solution) == 0:
            self.previousOperator = None
        else:
            self.previousOperator = solution[-1]

    def is_solved(self):
        solved = True
        previous = self.puzzle[0][0]
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                element = self.puzzle[i][j]
                if (i + 1) * (j + 1) == self.cols * self.rows:
                    if element != 0:
                        solved = False
                else:
                    if not element >= previous:
                        solved = False
                previous = element
        return solved

        # solved = True
        # n = self.puzzle[0][0]
        # for row in self.puzzle:
        #     for number in row:
        #         if not number >= n:
        #             solved = False
        #         n = number
        # return solved

    def move_left(self):
        newPuzzle = copy.deepcopy(self.puzzle)
        buffer = newPuzzle[self.YZero][self.XZero - 1]
        newPuzzle[self.YZero][self.XZero - 1] = 0
        newPuzzle[self.YZero][self.XZero] = buffer
        newNode = Node(newPuzzle, self.depth + 1, self.solution + 'L', self.cols, self.rows)
        return newNode

    def move_right(self):
        newPuzzle = copy.deepcopy(self.puzzle)
        buffer = newPuzzle[self.YZero][self.XZero + 1]
        newPuzzle[self.YZero][self.XZero + 1] = 0
        newPuzzle[self.YZero][self.XZero] = buffer
        newNode = Node(newPuzzle, self.depth + 1, self.solution + 'R', self.cols, self.rows)
        return newNode

    def move_up(self):
        newPuzzle = copy.deepcopy(self.puzzle)
        buffer = newPuzzle[self.YZero - 1][self.XZero]
        newPuzzle[self.YZero - 1][self.XZero] = 0
        newPuzzle[self.YZero][self.XZero] = buffer
        newNode = Node(newPuzzle, self.depth + 1, self.solution + 'U', self.cols, self.rows)
        return newNode

    def move_down(self):
        newPuzzle = copy.deepcopy(self.puzzle)
        buffer = newPuzzle[self.YZero + 1][self.XZero]
        newPuzzle[self.YZero + 1][self.XZero] = 0
        newPuzzle[self.YZero][self.XZero] = buffer
        newNode = Node(newPuzzle, self.depth + 1, self.solution + 'D', self.cols, self.rows)
        return newNode

    def can_move_left(self):
        if self.XZero != 0 and self.previousOperator != 'R':
            return True
        else:
            return False

    def can_move_right(self):
        if self.XZero < self.cols - 1 and self.previousOperator != 'L':
            return True
        else:
            return False

    def can_move_up(self):
        if self.YZero != 0 and self.previousOperator != 'D':
            return True
        else:
            return False

    def can_move_down(self):
        if self.YZero < self.rows - 1 and self.previousOperator != 'U':
            return True
        else:
            return False
