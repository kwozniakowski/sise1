class DFS:
    def __init__(self, depth_limit) -> None:
        self.max_reached_depth = 0
        self.depth_limit = depth_limit
        self.solution = None
        self.is_solved = False
        self.nodes = []
        self.checked_states = 0

    # TODO: Dorobić przetworzone stany

    def solve(self, root, order):
        is_solved = False
        self.nodes.append(root)
        while len(self.nodes) != 0 and is_solved == False:
            node = self.nodes.pop(-1)  # bierzemy zawsze ostatni dodany element
            self.checked_states = self.checked_states + 1
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

        if is_solved:
            print(self.solution.puzzle)
            print(self.solution.solution)
            print(len(self.solution.solution))  # dlugosc rozwiazania
            print("Odwiedzone stany: ", self.checked_states)
        else:
            print("Nie udalo sie znalezc rozwiazania")
