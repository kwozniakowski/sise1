from Node import Node
from BFS import BFS
from DFS import DFS
from AStar import AStar
from AStarNode import AStarNode
import pandas as pd
import time
import sys


def read_file(name):
    dimensions = pd.read_csv(name, nrows=1, header=None, delimiter=' ')
    input_rows = pd.read_csv(name, skiprows = [0], header=None, delimiter=' ')
    input_array = input_rows.values.tolist()
    r = dimensions[0].values[0]
    c = dimensions[1].values[0]
    return [input_array, c, r]


if __name__ == '__main__':
    strategy = sys.argv[1]
    additional_argument = sys.argv[2]
    input_file_name = sys.argv[3]
    output_solution_file_name = sys.argv[4]
    output_stats_file_name = sys.argv[5]

    data = read_file(input_file_name)
    puzzle = data[0]
    cols = data[1]
    rows = data[2]

    is_solved = False
    solution_length = 0
    solution_string = ''
    visited_states_number = 0
    processed_states_number = 0
    max_recursion_depth = 0
    elapsed_time = 0

    start = time.time() #TODO: Dopytać gdzie dokładnie start

    if strategy == 'bfs':
        order = additional_argument
        root = Node(puzzle, 0, '', cols, rows)
        bfsPuzzleSolver = BFS()
        bfsPuzzleSolver.solve(root, order)
        end = time.time()

        is_solved = bfsPuzzleSolver.is_solved
        solution_string = bfsPuzzleSolver.solution.solution
        solution_length = len(solution_string)
        visited_states_number = bfsPuzzleSolver.visited_states
        processed_states_number = bfsPuzzleSolver.processed_states
        max_recursion_depth = bfsPuzzleSolver.max_reached_depth
        elapsed_time = round(1000 * (end - start), 3) #TODO: Powielić dla DFS i AStar

    elif strategy == 'dfs':
        root = Node(puzzle, 0, '', cols, rows)
        order = additional_argument
        dfsPuzzleSolver = DFS(20)
        dfsPuzzleSolver.solve(root, order)
        end = time.time()

    elif strategy == 'astr':
        metric = additional_argument
        aStarPuzzleSolver = AStar()
        aStarRoot = AStarNode(puzzle, 0, '', metric, cols, rows)
        aStarPuzzleSolver.solve(aStarRoot, metric)
        end = time.time()

    else:
        print("Wrong strategy")
        exit(1)

    output_solution_file = open(output_solution_file_name, "w")
    output_stats_file = open(output_stats_file_name, "w")
    if not is_solved:
        output_solution_file.write("-1")
        output_stats_file.write("-1")

        output_solution_file.close()
        output_stats_file.close()
        exit(0)
    output_solution_file.write(str(solution_length) + "\n" + solution_string)
    output_stats_file.write(str(solution_length)+ "\n" + str(visited_states_number) + "\n"
                            + str(processed_states_number) + "\n" + str(max_recursion_depth) + "\n"
                            + str(elapsed_time))
