import matplotlib.pyplot as plt
import re
import os
import glob
import numpy as np

'''
possible_strategies = [
    'bfs',
    'dfs',
    'astr'
]

possible_orders = ['rdul', 'rdlu', 'drul', 'drlu', 'ludr', 'lurd', 'uldr', 'ulrd']
possible_tactics = ['hamm', 'manh']

files = os.listdir('/home/piotr/PycharmProjects/sise1/generate')
splitted_filenames = dict()

for x in possible_strategies[0:2]:
    splitted_filenames.update({x: possible_orders})
splitted_filenames.update({possible_strategies[2]: possible_tactics})

for x in range(1, 8):
    regex = '\dx\d_\d'+str(x)+'_\d{5}_bfs_rdul_stats.txt'
    regex_compiled = re.compile(regex)
    string = ''.join(files)
    match = re.findall(regex_compiled, string)
    steps = '0' + str(x)
    order = 'rdul'
    method = 'bfs'
'''

file_list = []
dfs= []
for name in glob.glob('generated/4x4_*_*_dfs_*_stats.txt'):
    # name = name[10:]
    # file_list.append(name)
    level = name[15]
    order = name[27:31]
    with open(name) as f:
        lines = f.readlines()
        solution_length = lines[0].strip()
        visited = lines[1].strip()
        processed = lines[2].strip()
        max_depth = lines[3].strip()
        time = lines[4].strip()

    dfs.append([level,order,solution_length,visited,processed,max_depth,time])

file_list = []
bfs= []
for name in glob.glob('4x4_0/4x4_*_*_bfs_*_stats.txt'):

    level = name[11]
    order = name[23:27]

    # level = name[15]
    # order = name[27:31]

    with open(name) as f:
        lines = f.readlines()
        solution_length = lines[0].strip()
        visited = lines[1].strip()
        processed = lines[2].strip()
        max_depth = lines[3].strip()
        time = lines[4].strip()

    bfs.append([level,order,solution_length,visited,processed,max_depth,time])

file_list = []
astr = []
for name in glob.glob('generated/4x4_*_*_astr_*_stats.txt'):
    # name = name[10:]
    # file_list.append(name)
    level = name[15]
    metric = name[28:32]
    with open(name) as f:
        lines = f.readlines()
        solution_length = lines[0].strip()
        visited = lines[1].strip()
        processed = lines[2].strip()
        max_depth = lines[3].strip()
        time = lines[4].strip()

    astr.append([level,metric,solution_length,visited,processed,max_depth,time])

strategies_set = ['rdul', 'rdlu', 'drul', 'drlu', 'ludr', 'lurd', 'uldr', 'ulrd']

def generate_bfs_charts(bfs):
    strategies_set = ['rdul', 'rdlu', 'drul', 'drlu', 'ludr', 'lurd', 'uldr', 'ulrd']
    time = []
    visited = []
    processed = []
    max_depth = []
    length = []
    for strategy in strategies_set:
        time_results = []
        visited_results = []
        processed_results = []
        max_depth_results = []
        length_results = []
        for i in range(1, 8):
            n = 0
            time_sum = 0
            visited_sum = 0
            processed_sum = 0
            length_sum = 0
            max_depth_sum = 0
            for dataset in bfs:
                if int(dataset[0]) == i and dataset[1] == strategy:
                    n = n + 1
                    time_sum = time_sum + float(dataset[6])
                    visited_sum = visited_sum + float(dataset[3])
                    processed_sum = processed_sum + float(dataset[4])
                    length_sum = length_sum + float(dataset[2])
                    max_depth_sum = max_depth_sum + float(dataset[5])
            time_results.append(time_sum / n / 1000)
            visited_results.append(visited_sum / n)
            processed_results.append(processed_sum / n)
            max_depth_results.append(max_depth_sum / n)
            length_results.append(length_sum / n)
        time.append(time_results)
        visited.append(visited_results)
        processed.append(processed_results)
        max_depth.append(max_depth_results)
        length.append(length_results)

    x= np.arange(start = 1, stop = 8)

    plt.cla()

    plt.bar(x-0.3, time[0], width=0.1, color='b', align='center', label = strategies_set[0])
    plt.bar(x-0.2, time[1], width=0.1, color='g', align='center', label = strategies_set[1])
    plt.bar(x-0.1, time[2], width=0.1, color='r', align='center', label = strategies_set[2])
    plt.bar(x, time[3], width=0.1, color='y', align='center', label = strategies_set[3])
    plt.bar(x+0.1, time[4], width=0.1, color='orange', align='center', label = strategies_set[4])
    plt.bar(x+0.2, time[5], width=0.1, color='purple', align='center', label = strategies_set[5])
    plt.bar(x+0.3, time[6], width=0.1, color='pink', align='center', label = strategies_set[6])
    plt.bar(x+0.4, time[7], width=0.1, color='black', align='center', label = strategies_set[7])

    plt.legend()
    plt.savefig('bfs_time.png')

    plt.cla()

    plt.bar(x - 0.3, visited[0], width=0.1, color='b', align='center', label=strategies_set[0])
    plt.bar(x - 0.2, visited[1], width=0.1, color='g', align='center', label=strategies_set[1])
    plt.bar(x - 0.1, visited[2], width=0.1, color='r', align='center', label=strategies_set[2])
    plt.bar(x, visited[3], width=0.1, color='y', align='center', label=strategies_set[3])
    plt.bar(x + 0.1, visited[4], width=0.1, color='orange', align='center', label=strategies_set[4])
    plt.bar(x + 0.2, visited[5], width=0.1, color='purple', align='center', label=strategies_set[5])
    plt.bar(x + 0.3, visited[6], width=0.1, color='pink', align='center', label=strategies_set[6])
    plt.bar(x + 0.4, visited[7], width=0.1, color='black', align='center', label=strategies_set[7])

    plt.legend()

    plt.savefig('bfs_visited.png')

    plt.cla()

    plt.bar(x - 0.3, processed[0], width=0.1, color='b', align='center', label=strategies_set[0])
    plt.bar(x - 0.2, processed[1], width=0.1, color='g', align='center', label=strategies_set[1])
    plt.bar(x - 0.1, processed[2], width=0.1, color='r', align='center', label=strategies_set[2])
    plt.bar(x, processed[3], width=0.1, color='y', align='center', label=strategies_set[3])
    plt.bar(x + 0.1, processed[4], width=0.1, color='orange', align='center', label=strategies_set[4])
    plt.bar(x + 0.2, processed[5], width=0.1, color='purple', align='center', label=strategies_set[5])
    plt.bar(x + 0.3, processed[6], width=0.1, color='pink', align='center', label=strategies_set[6])
    plt.bar(x + 0.4, processed[7], width=0.1, color='black', align='center', label=strategies_set[7])

    plt.legend()

    plt.savefig('bfs_processed.png')

    plt.cla()

    plt.bar(x - 0.3, length[0], width=0.1, color='b', align='center', label=strategies_set[0])
    plt.bar(x - 0.2, length[1], width=0.1, color='g', align='center', label=strategies_set[1])
    plt.bar(x - 0.1, length[2], width=0.1, color='r', align='center', label=strategies_set[2])
    plt.bar(x, length[3], width=0.1, color='y', align='center', label=strategies_set[3])
    plt.bar(x + 0.1, length[4], width=0.1, color='orange', align='center', label=strategies_set[4])
    plt.bar(x + 0.2, length[5], width=0.1, color='purple', align='center', label=strategies_set[5])
    plt.bar(x + 0.3, length[6], width=0.1, color='pink', align='center', label=strategies_set[6])
    plt.bar(x + 0.4, length[7], width=0.1, color='black', align='center', label=strategies_set[7])

    plt.legend()
    plt.savefig('bfs_length.png')

    plt.cla()

    plt.bar(x - 0.3, max_depth[0], width=0.1, color='b', align='center', label=strategies_set[0])
    plt.bar(x - 0.2, max_depth[1], width=0.1, color='g', align='center', label=strategies_set[1])
    plt.bar(x - 0.1, max_depth[2], width=0.1, color='r', align='center', label=strategies_set[2])
    plt.bar(x, max_depth[3], width=0.1, color='y', align='center', label=strategies_set[3])
    plt.bar(x + 0.1, max_depth[4], width=0.1, color='orange', align='center', label=strategies_set[4])
    plt.bar(x + 0.2, max_depth[5], width=0.1, color='purple', align='center', label=strategies_set[5])
    plt.bar(x + 0.3, max_depth[6], width=0.1, color='pink', align='center', label=strategies_set[6])
    plt.bar(x + 0.4, max_depth[7], width=0.1, color='black', align='center', label=strategies_set[7])

    plt.legend()
    plt.savefig('bfs_max_depth.png')


def generate_dfs_charts(dfs):
    strategies_set = ['rdul', 'rdlu', 'drul', 'drlu', 'ludr', 'lurd', 'uldr', 'ulrd']
    time = []
    visited = []
    processed = []
    max_depth = []
    length = []
    for strategy in strategies_set:
        time_results = []
        visited_results = []
        processed_results = []
        max_depth_results = []
        length_results = []
        for i in range(1, 8):
            n = 0
            time_sum = 0
            visited_sum = 0
            processed_sum = 0
            length_sum = 0
            max_depth_sum = 0
            for dataset in dfs:
                if int(dataset[0]) == i and dataset[1] == strategy:
                    n = n + 1
                    time_sum = time_sum + float(dataset[6])
                    visited_sum = visited_sum + float(dataset[3])
                    processed_sum = processed_sum + float(dataset[4])
                    length_sum = length_sum + float(dataset[2])
                    max_depth_sum = max_depth_sum + float(dataset[5])
            time_results.append(time_sum / n / 1000)
            visited_results.append(visited_sum / n)
            processed_results.append(processed_sum / n)
            max_depth_results.append(max_depth_sum / n)
            length_results.append(length_sum / n)
        time.append(time_results)
        visited.append(visited_results)
        processed.append(processed_results)
        max_depth.append(max_depth_results)
        length.append(length_results)

    x= np.arange(start = 1, stop = 8)

    plt.cla()

    plt.bar(x-0.3, time[0], width=0.1, color='b', align='center', label = strategies_set[0])
    plt.bar(x-0.2, time[1], width=0.1, color='g', align='center', label = strategies_set[1])
    plt.bar(x-0.1, time[2], width=0.1, color='r', align='center', label = strategies_set[2])
    plt.bar(x, time[3], width=0.1, color='y', align='center', label = strategies_set[3])
    plt.bar(x+0.1, time[4], width=0.1, color='orange', align='center', label = strategies_set[4])
    plt.bar(x+0.2, time[5], width=0.1, color='purple', align='center', label = strategies_set[5])
    plt.bar(x+0.3, time[6], width=0.1, color='pink', align='center', label = strategies_set[6])
    plt.bar(x+0.4, time[7], width=0.1, color='black', align='center', label = strategies_set[7])

    plt.legend()
    plt.yscale("log")
    plt.savefig('dfs_time.png')

    plt.cla()

    plt.bar(x - 0.3, visited[0], width=0.1, color='b', align='center', label=strategies_set[0])
    plt.bar(x - 0.2, visited[1], width=0.1, color='g', align='center', label=strategies_set[1])
    plt.bar(x - 0.1, visited[2], width=0.1, color='r', align='center', label=strategies_set[2])
    plt.bar(x, visited[3], width=0.1, color='y', align='center', label=strategies_set[3])
    plt.bar(x + 0.1, visited[4], width=0.1, color='orange', align='center', label=strategies_set[4])
    plt.bar(x + 0.2, visited[5], width=0.1, color='purple', align='center', label=strategies_set[5])
    plt.bar(x + 0.3, visited[6], width=0.1, color='pink', align='center', label=strategies_set[6])
    plt.bar(x + 0.4, visited[7], width=0.1, color='black', align='center', label=strategies_set[7])

    plt.legend()
    plt.yscale("log")
    plt.savefig('dfs_visited.png')

    plt.cla()

    plt.bar(x - 0.3, processed[0], width=0.1, color='b', align='center', label=strategies_set[0])
    plt.bar(x - 0.2, processed[1], width=0.1, color='g', align='center', label=strategies_set[1])
    plt.bar(x - 0.1, processed[2], width=0.1, color='r', align='center', label=strategies_set[2])
    plt.bar(x, processed[3], width=0.1, color='y', align='center', label=strategies_set[3])
    plt.bar(x + 0.1, processed[4], width=0.1, color='orange', align='center', label=strategies_set[4])
    plt.bar(x + 0.2, processed[5], width=0.1, color='purple', align='center', label=strategies_set[5])
    plt.bar(x + 0.3, processed[6], width=0.1, color='pink', align='center', label=strategies_set[6])
    plt.bar(x + 0.4, processed[7], width=0.1, color='black', align='center', label=strategies_set[7])

    plt.legend()
    plt.yscale("log")
    plt.savefig('dfs_processed.png')

    plt.cla()

    plt.bar(x - 0.3, length[0], width=0.1, color='b', align='center', label=strategies_set[0])
    plt.bar(x - 0.2, length[1], width=0.1, color='g', align='center', label=strategies_set[1])
    plt.bar(x - 0.1, length[2], width=0.1, color='r', align='center', label=strategies_set[2])
    plt.bar(x, length[3], width=0.1, color='y', align='center', label=strategies_set[3])
    plt.bar(x + 0.1, length[4], width=0.1, color='orange', align='center', label=strategies_set[4])
    plt.bar(x + 0.2, length[5], width=0.1, color='purple', align='center', label=strategies_set[5])
    plt.bar(x + 0.3, length[6], width=0.1, color='pink', align='center', label=strategies_set[6])
    plt.bar(x + 0.4, length[7], width=0.1, color='black', align='center', label=strategies_set[7])

    plt.legend()
    plt.savefig('dfs_length.png')

    plt.cla()

    plt.bar(x - 0.3, max_depth[0], width=0.1, color='b', align='center', label=strategies_set[0])
    plt.bar(x - 0.2, max_depth[1], width=0.1, color='g', align='center', label=strategies_set[1])
    plt.bar(x - 0.1, max_depth[2], width=0.1, color='r', align='center', label=strategies_set[2])
    plt.bar(x, max_depth[3], width=0.1, color='y', align='center', label=strategies_set[3])
    plt.bar(x + 0.1, max_depth[4], width=0.1, color='orange', align='center', label=strategies_set[4])
    plt.bar(x + 0.2, max_depth[5], width=0.1, color='purple', align='center', label=strategies_set[5])
    plt.bar(x + 0.3, max_depth[6], width=0.1, color='pink', align='center', label=strategies_set[6])
    plt.bar(x + 0.4, max_depth[7], width=0.1, color='black', align='center', label=strategies_set[7])

    plt.legend()
    plt.savefig('dfs_max_depth.png')


def generate_astr_charts(astr):
    metrics_set = ['hamm', 'manh']
    time = []
    visited = []
    processed = []
    max_depth = []
    length = []
    for metric in metrics_set:
        time_results = []
        visited_results = []
        processed_results = []
        max_depth_results = []
        length_results = []
        for i in range(1, 8):
            n = 0
            time_sum = 0
            visited_sum = 0
            processed_sum = 0
            length_sum = 0
            max_depth_sum = 0
            for dataset in astr:
                if int(dataset[0]) == i and dataset[1] == metric:
                    n = n + 1
                    time_sum = time_sum + float(dataset[6])
                    visited_sum = visited_sum + float(dataset[3])
                    processed_sum = processed_sum + float(dataset[4])
                    length_sum = length_sum + float(dataset[2])
                    max_depth_sum = max_depth_sum + float(dataset[5])
            time_results.append(time_sum / n / 1000)
            visited_results.append(visited_sum / n )
            processed_results.append(processed_sum / n )
            max_depth_results.append(max_depth_sum / n )
            length_results.append(length_sum / n )
        time.append(time_results)
        visited.append(visited_results)
        processed.append(processed_results)
        max_depth.append(max_depth_results)
        length.append(length_results)

    x = np.arange(start=1, stop=8)

    plt.cla()

    plt.bar(x - 0.3, time[0], width=0.3, color='b', align='center', label=metrics_set[0])
    plt.bar(x, time[1], width=0.3, color='g', align='center', label=metrics_set[1])

    plt.legend()
    plt.savefig("astr_time.png")

    plt.cla()

    plt.bar(x - 0.3, visited[0], width=0.3, color='b', align='center', label=metrics_set[0])
    plt.bar(x, visited[1], width=0.3, color='g', align='center', label=metrics_set[1])

    plt.legend()
    plt.savefig("astr_visited.png")

    plt.cla()


    plt.bar(x - 0.3, processed[0], width=0.3, color='b', align='center', label=metrics_set[0])
    plt.bar(x, processed[1], width=0.3, color='g', align='center', label=metrics_set[1])

    plt.legend()
    plt.savefig("astr_processed.png")

    plt.cla()

    plt.bar(x - 0.3, max_depth[0], width=0.3, color='b', align='center', label=metrics_set[0])
    plt.bar(x, max_depth[1], width=0.3, color='g', align='center', label=metrics_set[1])

    plt.legend()
    plt.savefig("astr_max_depth.png")

    plt.cla()

    plt.bar(x - 0.3, length[0], width=0.3, color='b', align='center', label=metrics_set[0])
    plt.bar(x, length[1], width=0.3, color='g', align='center', label=metrics_set[1])

    plt.legend()
    plt.savefig("astr_length.png")



generate_dfs_charts(dfs)
generate_astr_charts(astr)
generate_bfs_charts(bfs)


