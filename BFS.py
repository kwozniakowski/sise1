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
            for i in range(4):
                direction = order[i]
                if direction == 'L':
                    if node.canMoveLeft():
                        newNode = node.moveLeft()
                        puzzle_tuple = self.generate_tuple_from_puzzle(newNode.puzzle)
                        if puzzle_tuple not in explored:
                            nodes.append(newNode)
                            explored.add(puzzle_tuple)

                elif direction == 'R':
                    if node.canMoveRight():
                        newNode = node.moveRight()
                        puzzle_tuple = self.generate_tuple_from_puzzle(newNode.puzzle)
                        if puzzle_tuple not in explored:
                            nodes.append(newNode)
                        explored.add(puzzle_tuple)

                elif direction == 'U':
                    if node.canMoveUp():
                        newNode = node.moveUp()
                        puzzle_tuple = self.generate_tuple_from_puzzle(newNode.puzzle)
                        if puzzle_tuple not in explored:
                            nodes.append(newNode)
                            explored.add(puzzle_tuple)

                else:
                    if node.canMoveDown():
                        newNode = node.moveDown()
                        puzzle_tuple = self.generate_tuple_from_puzzle(newNode.puzzle)
                        if puzzle_tuple not in explored:
                            nodes.append(newNode)
                            explored.add(puzzle_tuple)
                if nodes[-1].isSolved():
                    isSolved = True
                    solution = nodes[-1]

        if isSolved:
            print(solution.puzzle)
            print(solution.solution)
            print("Przetworzone stany: ", checkedStates)
            print("Odwiedzone stany: ", checkedStates + len(nodes)) #TODO: tutaj zmienić, żeby odpowiednio wyświetlało wartości
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
