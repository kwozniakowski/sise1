from operator import attrgetter
class AStar:
    def __init__(self, metric) -> None:
        self.processed_states = None
        self.visited_states = None
        self.max_reached_depth = 0
        self.solution = None
        self.is_solved = False
        self.nodes = []
        self.metric = metric

    def solve(self, root):
        self.processed_states = 0
        self.nodes.append(root)
        while len(self.nodes) != 0 and not self.is_solved:
            self.nodes.sort(key=attrgetter('total_distance','depth'))
            node = self.nodes.pop(0)
            self.processed_states += 1

            if self.max_reached_depth < node.depth:
                self.max_reached_depth = node.depth

            if node.is_solved():
                self.is_solved = True
                self.solution = node
            if node.can_move_left():
                new_node = node.move_left()
                self.check_if_solved(new_node)
                self.determine_max_depth(new_node)
                self.nodes.append(new_node)
            if node.can_move_right():
                new_node = node.move_right()
                self.check_if_solved(new_node)
                self.determine_max_depth(new_node)
                self.nodes.append(new_node)
            if node.can_move_up():
                new_node = node.move_up()
                self.check_if_solved(new_node)
                self.determine_max_depth(new_node)
                self.nodes.append(new_node)
            if node.can_move_down():
                new_node = node.move_down()
                self.check_if_solved(new_node)
                self.determine_max_depth(new_node)
                self.nodes.append(new_node)

        self.visited_states = self.processed_states + len(self.nodes)


    def get_total_distance(self, node):
        return node.total_distance

    def check_if_solved(self, node):
        if node.is_solved():
            self.is_solved = True
            self.solution = node

    def determine_max_depth(self, node):
        if node.depth > self.max_reached_depth:
            self.max_reached_depth = node.depth
