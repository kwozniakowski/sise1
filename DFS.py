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
        self.processed_states = 0
        while len(self.nodes) != 0 and not self.is_solved:
            node = self.nodes.pop(-1)  # bierzemy zawsze ostatni dodany element
            # self.visited_states = self.visited_states + 1
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
                            new_node = node.move_left()
                            self.check_if_solved(new_node)
                            self.determine_max_depth(new_node)
                            self.nodes.append(new_node)
                    if direction == 'R':
                        if node.can_move_right():
                            new_node = node.move_right()
                            self.check_if_solved(new_node)
                            self.determine_max_depth(new_node)
                            self.nodes.append(new_node)
                    if direction == 'U':
                        if node.can_move_up():
                            new_node = node.move_up()
                            self.check_if_solved(new_node)
                            self.determine_max_depth(new_node)
                            self.nodes.append(new_node)
                    if direction == 'D':
                        if node.can_move_down():
                            new_node = node.move_down()
                            self.check_if_solved(new_node)
                            self.determine_max_depth(new_node)
                            self.nodes.append(new_node)
            self.processed_states = self.processed_states + 1
        self.visited_states = self.processed_states + len(self.nodes)


    def check_if_solved(self, node):
        if node.is_solved():
            self.is_solved = True
            self.solution = node

    def determine_max_depth(self, node):
        if node.depth > self.max_reached_depth:
            self.max_reached_depth = node.depth
