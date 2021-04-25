MAX_DEPTH = 9
class DFS :
    moves = 0

    def solve(self,root,order):
        nodes = []
        checkedStates = 0
        solution = None
        isSolved = False
        nodes.append(root)
        while len(nodes) != 0 and isSolved == False:
            node = nodes.pop(-1) #bierzemy zawsze ostatni dodany element
            checkedStates = checkedStates + 1
            if node.isSolved():
                isSolved = True
                solution = node
            if node.depth < MAX_DEPTH:
                for i in range(0, 4):
                    direction = order[i]
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
        if isSolved :
            print(solution.puzzle)
            print(solution.solution)
            print(len(solution.solution)) # dlugosc rozwiazania
            print("Odwiedzone stany: ", checkedStates)
        else :
            print("Nie udalo sie znalezc rozwiazania")
