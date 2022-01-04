"""
This is a code for implenting the dijsktra shortest path algorithm

1/2/21
"""
import sys


def dijsktra(graph, src, dest):
    inf = sys.maxsize
    node_data = {
        'A': {'cost': inf, 'path': []},
        'B': {'cost': inf, 'path': []},
        'C': {'cost': inf, 'path': []},
        'D': {'cost': inf, 'path': []},
        'E': {'cost': inf, 'path': []},
        'F': {'cost': inf, 'path': []}
    }
    node_data[src]['cost'] = 0
    visited = []
    temp_arr = []
    done = False
    selected_node = src
    for i in graph:
        temp_arr = []
        for node in graph:
            if node is selected_node:
                visited.append(node)
                for node_dist in graph[node]:
                    temp_cost = graph[node][node_dist] + node_data[node]['cost']
                    if temp_cost < node_data[node_dist]['cost']:
                        node_data[node_dist]['cost'] = graph[node][node_dist] + node_data[node]['cost']
                        node_data[node_dist]['path'] = [node]
        for node in graph:
            if node not in visited:
                temp_arr.append([node_data[node]['cost']])
        temp_min = min(temp_arr)
        temp_min = temp_min[0]
        for node in graph:
            if node_data[node]['cost'] is temp_min and not done and node not in visited:
                selected_node = node
                done = True
        done = False

        if selected_node is dest:
            for node in graph:
                for i in graph:
                    if i in node_data[node]['path']:
                        val = node_data[i]['path']
                        if len(val) > 0:
                            for j in range(len(val)):
                                node_data[node]['path'].append(val[j])
            print(node_data)
            return
    return


graph = {
    'A': {'B': 4,  'C': 3},
    'B': {'A': 4,  'C': 3,  'D': 3},
    'C': {'A': 3,  'B': 3,  'E': 5,  'D': 2},
    'D': {'B': 3,  'C': 2,  'E': 11, 'F': 12},
    'E': {'C': 5,  'D': 11, 'F': 10},
    'F': {'D': 12, 'E': 10}
}

source = 'A'
destination = 'F'

dijsktra(graph, source, destination)
