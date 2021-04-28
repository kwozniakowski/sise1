class BFS:
    def solve(self, root, order):
        nodes = []
        explored = set()
        solution = ''
        checkedStates = 0
        isSolved = False
        nodes.append(root)
        while len(nodes) != 0 and not isSolved:
            node = nodes.pop(0)
            # if puzzle_tuple not in explored:
            checkedStates = checkedStates + 1
            if node.isSolved():
                isSolved = True
                solution = node
            for i in range(4):
                direction = order[i]
                # puzzle_tuple = self.generate_tuple_from_puzzle(node.puzzle)
                if direction == 'L':
                    if node.canMoveLeft():
                        newNode = node.moveLeft()
                        nodes.append(newNode)
                if direction == 'R':
                    if node.canMoveRight():
                        newNode = node.moveRight()
                        nodes.append(newNode)
                if direction == 'U':
                    if node.canMoveUp():
                        newNode = node.moveUp()
                        nodes.append(newNode)
                if direction == 'D':
                    if node.canMoveDown():
                        newNode = node.moveDown()
                        nodes.append(newNode)
                # explored.add(puzzle_tuple)
        if isSolved:
            print(solution.puzzle)
            print(solution.solution)
            print("Przetworzone stany: ", checkedStates)
            print("Odwiedzone stany: ", checkedStates + len(nodes))
            print(solution.depth)
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
