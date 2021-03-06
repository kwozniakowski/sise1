class BFS :
    def solve(self,root,order):
        nodes = []
        explored = []
        solution = ''
        checkedStates = 0
        isSolved = False
        nodes.append(root)
        while len(nodes) != 0 and isSolved == False:
            node = nodes.pop(0)
            if hash(str(node.puzzle)) not in explored :
                checkedStates = checkedStates + 1
                if node.isSolved():
                    isSolved = True
                    solution = node
                for i in range (0,4) :
                    direction = order[i]
                    if direction == 'L' :
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
                explored.append(hash(str(node.puzzle)))
        if isSolved :
            print(solution.puzzle)
            print(solution.solution)
            print("Przetworzone stany: ", checkedStates)
            print("Odwiedzone stany: ", checkedStates + len(nodes))
            print(solution.depth)
        else :
            print("Nie udalo sie znalezc rozwiazania")
