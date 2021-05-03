class BFS:
    def __init__(self) -> None:
        super().__init__()
        self.solution = None
        self.nodes = []
        self.explored = set()
        self.is_solved = False

    def solve(self, root, order):
        processed_states = 0
        self.nodes.append(root)
        while len(self.nodes) != 0 and not self.is_solved:
            node = self.nodes.pop(0)
            for i in range(4):
                direction = order[i]
                if direction == 'L':
                    if node.canMoveLeft():
                        new_node = node.moveLeft()
                        self.check_if_solved(new_node)
                        puzzle_tuple = self.generate_tuple_from_puzzle(new_node.puzzle)
                        self.process_puzzle_tuple(puzzle_tuple, new_node)
                elif direction == 'R':
                    if node.canMoveRight():
                        new_node = node.moveRight()
                        self.check_if_solved(new_node)
                        puzzle_tuple = self.generate_tuple_from_puzzle(new_node.puzzle)
                        self.process_puzzle_tuple(puzzle_tuple, new_node)

                elif direction == 'U':
                    if node.canMoveUp():
                        new_node = node.moveUp()
                        self.check_if_solved(new_node)
                        puzzle_tuple = self.generate_tuple_from_puzzle(new_node.puzzle)
                        self.process_puzzle_tuple(puzzle_tuple, new_node)
                else:
                    if node.canMoveDown():
                        new_node = node.moveDown()
                        self.check_if_solved(new_node)
                        puzzle_tuple = self.generate_tuple_from_puzzle(new_node.puzzle)
                        self.process_puzzle_tuple(puzzle_tuple, new_node)

            processed_states = processed_states + 1

        if self.is_solved:
            print(self.solution.puzzle)
            print(self.solution.solution)
            print("Przetworzone stany: ", processed_states)
            print("Odwiedzone stany: ", processed_states + len(self.nodes))
            print(self.solution.depth)
        else:
            print("Nie udalo sie znalezc rozwiazania")

    @staticmethod
    def generate_tuple_from_puzzle(puzzle):
        one_dimensional_list = []
        for i in puzzle:
            for j in i:
                one_dimensional_list.append(j)
        result_tuple = tuple(one_dimensional_list)
        return result_tuple

    def process_puzzle_tuple(self, puzzle_tuple, node):
        if puzzle_tuple not in self.explored:
            self.nodes.append(node)
            self.explored.add(puzzle_tuple)

    def check_if_solved(self, node):
        if node.isSolved():
            self.is_solved = True
            self.solution = node
