import os, sys, time

def parse_input(lines):
    graph = {}
    landmarks = {}
    for line in [l.strip() for l in lines]:
        if line.startswith('('):
            for tup in [l.strip('()').split(',') for l in line.replace(' ', '').split('),(')]:
                tup = [int(t) for t in tup]
                if tup[0] not in graph:
                    graph[tup[0]] = {}
                if tup[1] not in graph:
                    graph[tup[1]] = {}
                graph[tup[0]][tup[1]] = tup[2]
                graph[tup[1]][tup[0]] = tup[2]
        elif len(line):
            line = [int(l.strip()) for l in line.split(' ')]
            landmarks[line[0]] = {}
            for index, val in zip(range(0, len(line) - 1), line[1:]):
                landmarks[line[0]][index] = val
    return graph, landmarks

def djikstra_heuristic(graph, landmarks, node):
    return 0

def landmarks_heuristic(graph, landmarks, node):
    return max([v[node] for k, v in landmarks.items()])

def a_star(graph, landmarks, start, end, heuristic):
    nodes = {}
    for i in list(graph.keys()):
        nodes[i] = {'distance': sys.maxsize, 'visited': False, 'previous': None}
    nodes[start]['distance'] = 0
    current_node = start
    while not nodes[end]['visited'] and min([v['distance'] for v in [v for v in list(nodes.values()) if not v['visited']]]) != sys.maxsize:
        for i in list(graph[current_node].keys()):
            if nodes[current_node]['distance'] + graph[current_node][i] < nodes[i]['distance']:
                nodes[i]['distance'] = nodes[current_node]['distance'] + graph[current_node][i]
                nodes[i]['previous'] = current_node
        nodes[current_node]['visited'] = True

        if current_node == end:
            break

        # Determine the next node using the given heuristic
        minimum_score = sys.maxsize
        for key, node in {k: v for k, v in nodes.items() if not v['visited'] and v['distance'] != sys.maxsize}.items():
            score = node['distance'] + heuristic(graph, landmarks, key)
            if score <= minimum_score:
                minimum_score = score
                current_node = key

    shortest_path = [end]
    u = nodes[end]['previous']
    while u is not None:
        shortest_path.append(u)
        u = nodes[u]['previous']
    shortest_path.reverse()

    return shortest_path

_GRAPH, _LANDMARKS = parse_input(sys.stdin.readlines())

start = time.clock()
_DJIKSTRA_SOLN = a_star(_GRAPH, _LANDMARKS,
                        min([key for key in list(_GRAPH.keys())]),
                        max([key for key in list(_GRAPH.keys())]),
                        djikstra_heuristic)
end = time.clock()
print('Djikstra Solution:\t{}'.format(' '.join([str(i) for i in _DJIKSTRA_SOLN])))
print("Time: {}us".format(int((end - start) * 10**6)))

start = time.clock()
_LANDMARKS_SOLN = a_star(_GRAPH, _LANDMARKS,
                        min([key for key in list(_GRAPH.keys())]),
                        max([key for key in list(_GRAPH.keys())]),
                        landmarks_heuristic)
end = time.clock()
print('Landmarks Solution:\t{}'.format(' '.join([str(i) for i in _LANDMARKS_SOLN])))
print("Time: {}us".format(int((end - start) * 10**6)))

