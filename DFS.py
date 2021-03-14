MAX_DEPTH = 30
class DFS :
    moves = 0

    def solve(self,root):
        nodes = []
        checkedStates = 0
        solution = None
        isSolved = False
        nodes.append(root)
        while len(nodes) != 0 and isSolved == False:
            node = nodes.pop(-1) #bierzemy zawsze ostatni dodany element
            checkedStates = checkedStates + 1
            print(node.puzzle)
            if node.depth < MAX_DEPTH:
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
