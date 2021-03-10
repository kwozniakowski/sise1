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
            if node.isSolved():
                isSolved = True
                solution = node
            if node.canMoveLeft():
                newNode = node.moveLeft()
                nodes.append(newNode)
            if node.canMoveRight():
                newNode = node.moveRight()
                nodes.append(newNode)
            if node.canMoveUp():
                newNode = node.moveUp()
                nodes.append(newNode)
            if node.canMoveDown():
                newNode = node.moveDown()
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