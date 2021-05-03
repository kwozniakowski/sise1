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
            if node.is_solved():
                isSolved = True
                solution = node
            if node.depth < MAX_DEPTH:
                for i in range(0, 4):
                    direction = order[i]
                    if direction == 'L':
                        if node.can_move_left():
                            newNode = node.move_left()
                            nodes.append(newNode)
                    if direction == 'R':
                        if node.can_move_right():
                            newNode = node.move_right()
                            nodes.append(newNode)
                    if direction == 'U':
                        if node.can_move_up():
                            newNode = node.move_up()
                            nodes.append(newNode)
                    if direction == 'D':
                        if node.can_move_down():
                            newNode = node.move_down()
                            nodes.append(newNode)
        if isSolved :
            print(solution.puzzle)
            print(solution.solution)
            print(len(solution.solution)) # dlugosc rozwiazania
            print("Odwiedzone stany: ", checkedStates)
        else :
            print("Nie udalo sie znalezc rozwiazania")
