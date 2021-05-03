class BFS:
    def solve(self, root, order):
        nodes = []
        explored = set()
        solution = ''
        processed_states = 0
        is_solved = False
        nodes.append(root)
        while len(nodes) != 0 and not is_solved:
            node = nodes.pop(0)
            for i in range(4):
                direction = order[i]
                if direction == 'L':
                    if node.canMoveLeft():
                        new_node = node.moveLeft()
                        if new_node.isSolved():
                            is_solved = True
                            solution = new_node
                        puzzle_tuple = self.generate_tuple_from_puzzle(new_node.puzzle)
                        if puzzle_tuple not in explored:
                            nodes.append(new_node)
                            explored.add(puzzle_tuple)

                elif direction == 'R':
                    if node.canMoveRight():
                        new_node = node.moveRight()
                        if new_node.isSolved():
                            is_solved = True
                            solution = new_node
                        puzzle_tuple = self.generate_tuple_from_puzzle(new_node.puzzle)
                        if puzzle_tuple not in explored:
                            nodes.append(new_node)
                            explored.add(puzzle_tuple)

                elif direction == 'U':
                    if node.canMoveUp():
                        new_node = node.moveUp()
                        if new_node.isSolved():
                            is_solved = True
                            solution = new_node
                        puzzle_tuple = self.generate_tuple_from_puzzle(new_node.puzzle)
                        if puzzle_tuple not in explored:
                            nodes.append(new_node)
                            explored.add(puzzle_tuple)

                else:
                    if node.canMoveDown():
                        new_node = node.moveDown()
                        if new_node.isSolved():
                            is_solved = True
                            solution = new_node
                        puzzle_tuple = self.generate_tuple_from_puzzle(new_node.puzzle)
                        if puzzle_tuple not in explored:
                            nodes.append(new_node)
                            explored.add(puzzle_tuple)
            processed_states = processed_states + 1


        if is_solved:
            print(solution.puzzle)
            print(solution.solution)
            print("Przetworzone stany: ", processed_states)
            print("Odwiedzone stany: ",  processed_states + len(nodes))
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
