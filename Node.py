import copy


class Node:
    def __init__(self, puzzle, depth, solution, cols, rows):
        self.cols = cols
        self.rows = rows
        self.puzzle = puzzle
        for i in range(0, len(puzzle)):
            for j in range(0, len(puzzle[i])):
                if puzzle[i][j] == 0:
                    self.x_zero = j
                    self.y_zero = i
        self.depth = depth
        self.solution = solution
        if len(solution) == 0:
            self.previous_operator = None
        else:
            self.previous_operator = solution[-1]

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

    def move_left(self):
        new_puzzle = copy.deepcopy(self.puzzle)
        buffer = new_puzzle[self.y_zero][self.x_zero - 1]
        new_puzzle[self.y_zero][self.x_zero - 1] = 0
        new_puzzle[self.y_zero][self.x_zero] = buffer
        newNode = Node(new_puzzle, self.depth + 1, self.solution + 'L', self.cols, self.rows)
        return newNode

    def move_right(self):
        new_puzzle = copy.deepcopy(self.puzzle)
        buffer = new_puzzle[self.y_zero][self.x_zero + 1]
        new_puzzle[self.y_zero][self.x_zero + 1] = 0
        new_puzzle[self.y_zero][self.x_zero] = buffer
        newNode = Node(new_puzzle, self.depth + 1, self.solution + 'R', self.cols, self.rows)
        return newNode

    def move_up(self):
        new_puzzle = copy.deepcopy(self.puzzle)
        buffer = new_puzzle[self.y_zero - 1][self.x_zero]
        new_puzzle[self.y_zero - 1][self.x_zero] = 0
        new_puzzle[self.y_zero][self.x_zero] = buffer
        newNode = Node(new_puzzle, self.depth + 1, self.solution + 'U', self.cols, self.rows)
        return newNode

    def move_down(self):
        new_puzzle = copy.deepcopy(self.puzzle)
        buffer = new_puzzle[self.y_zero + 1][self.x_zero]
        new_puzzle[self.y_zero + 1][self.x_zero] = 0
        new_puzzle[self.y_zero][self.x_zero] = buffer
        newNode = Node(new_puzzle, self.depth + 1, self.solution + 'D', self.cols, self.rows)
        return newNode

    def can_move_left(self):
        if self.x_zero != 0 and self.previous_operator != 'R':
            return True
        else:
            return False

    def can_move_right(self):
        if self.x_zero < self.cols - 1 and self.previous_operator != 'L':
            return True
        else:
            return False

    def can_move_up(self):
        if self.y_zero != 0 and self.previous_operator != 'D':
            return True
        else:
            return False

    def can_move_down(self):
        if self.y_zero < self.rows - 1 and self.previous_operator != 'U':
            return True
        else:
            return False
