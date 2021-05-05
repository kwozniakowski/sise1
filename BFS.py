class BFS:
    def __init__(self) -> None:
        self.solution = None
        self.nodes = []
        self.explored = set()
        self.is_solved = False
        self.processed_states = 0
        self.visited_states = 0
        self.max_reached_depth = 0

    def solve(self, root, order):
        self.nodes.append(root)
        while len(self.nodes) != 0 and not self.is_solved:
            node = self.nodes.pop(0)
            for i in range(4):
                direction = order[i]
                if direction == 'L':
                    if node.can_move_left():
                        new_node = node.move_left()
                        self.check_if_solved(new_node)
                        puzzle_tuple = self.generate_tuple_from_puzzle(new_node.puzzle)
                        self.process_puzzle_tuple(puzzle_tuple, new_node)
                elif direction == 'R':
                    if node.can_move_right():
                        new_node = node.move_right()
                        self.check_if_solved(new_node)
                        puzzle_tuple = self.generate_tuple_from_puzzle(new_node.puzzle)
                        self.process_puzzle_tuple(puzzle_tuple, new_node)

                elif direction == 'U':
                    if node.can_move_up():
                        new_node = node.move_up()
                        self.check_if_solved(new_node)
                        puzzle_tuple = self.generate_tuple_from_puzzle(new_node.puzzle)
                        self.process_puzzle_tuple(puzzle_tuple, new_node)
                else:
                    if node.can_move_down():
                        new_node = node.move_down()
                        self.check_if_solved(new_node)
                        puzzle_tuple = self.generate_tuple_from_puzzle(new_node.puzzle)
                        self.process_puzzle_tuple(puzzle_tuple, new_node)

            self.processed_states = self.processed_states + 1

        if self.is_solved:
            self.visited_states = self.processed_states + len(self.nodes)
            self.max_reached_depth = self.solution.depth

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
        if node.is_solved():
            self.is_solved = True
            self.solution = node
