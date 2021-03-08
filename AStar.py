class AStar :
    def solve(self,root):
        nodes = []
        checkedStates = 0
        solution = None
        isSolved = False
        nodes.append(root)
        while len(nodes) != 0 and isSolved == False:
            minDistance = nodes[0].manhattanDistance + nodes[0].depth
            node = nodes[0]
            for aStarNode in nodes :
                print (aStarNode.manhattanDistance)
                if (aStarNode.manhattanDistance + aStarNode.depth) < minDistance:
                    minDistance = aStarNode.manhattanDistance + aStarNode.depth
                    node = aStarNode
                checkedStates = checkedStates + 1
            nodes.clear()
            print('wybrano',node.manhattanDistance)
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
        else :
            print("Nie udalo sie znalezc rozwiazania")
