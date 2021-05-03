class DFS:
    def __init__(self, depth_limit) -> None:
        self.processed_states = None
        self.visited_states = None
        self.max_reached_depth = 0
        self.depth_limit = depth_limit
        self.solution = None
        self.is_solved = False
        self.nodes = []
        self.visited_states = 0

    # TODO: Dorobić przetworzone stany jako self.processed_states

    def solve(self, root, order):
        self.nodes.append(root)
        while len(self.nodes) != 0 and not self.is_solved:
            node = self.nodes.pop(-1)  # bierzemy zawsze ostatni dodany element
            self.visited_states = self.visited_states + 1
            if node.is_solved():
                self.is_solved = True
                self.solution = node
            if self.max_reached_depth < node.depth:
                self.max_reached_depth = node.depth
            if node.depth < self.depth_limit:
                for i in range(0, 4):
                    direction = order[i]
                    if direction == 'L':
                        if node.can_move_left():
                            newNode = node.move_left()
                            self.nodes.append(newNode)
                    if direction == 'R':
                        if node.can_move_right():
                            newNode = node.move_right()
                            self.nodes.append(newNode)
                    if direction == 'U':
                        if node.can_move_up():
                            newNode = node.move_up()
                            self.nodes.append(newNode)
                    if direction == 'D':
                        if node.can_move_down():
                            newNode = node.move_down()
                            self.nodes.append(newNode)

        if self.is_solved:
            print(self.solution.puzzle)
            print(self.solution.solution)
            print(len(self.solution.solution))  # dlugosc rozwiazania
            print("Odwiedzone stany: ", self.visited_states)
        else:
            print("Nie udalo sie znalezc rozwiazania")
