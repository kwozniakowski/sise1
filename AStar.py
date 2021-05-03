class AStar :
    def solve(self,root,metric):
        nodes = []
        checkedStates = 0
        solution = None
        isSolved = False
        nodes.append(root)
        while len(nodes) != 0 and isSolved == False:
            nodes.sort(key=self.getTotalDistance)
            node = nodes.pop(0)
            checkedStates += 1
            if node.is_solved():
                isSolved = True
                solution = node
            if node.can_move_left():
                newNode = node.move_left()
                nodes.append(newNode)
            if node.can_move_right():
                newNode = node.move_right()
                nodes.append(newNode)
            if node.can_move_up():
                newNode = node.move_up()
                nodes.append(newNode)
            if node.can_move_down():
                newNode = node.move_down()
                nodes.append(newNode)
        if isSolved :
            print(solution.puzzle)
            print(solution.solution)
            print("Odwiedzone stany: ", checkedStates)
            print("Głębokość rozwiazania: ", solution.depth)
        else :
            print("Nie udalo sie znalezc rozwiazania")

    def getTotalDistance(self, node):
        return node.totalDistance