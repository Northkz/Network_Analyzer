

from heapq import heappush, heappop
from graph import Graph


def single_source_shortest_paths_dijkstra(graph: Graph, source: int, cutoff=None):


    adj_list = graph.adj_list

    distances = {}

    paths = dict.fromkeys(graph.nodes, [])
    paths[source] = [[source]]

    predecessors = dict()

    visited = dict()
    visited[source] = 0

    heap = []
    heappush(heap, (0, source, source))

    while heap:
        (distance, pred, v) = heappop(heap)

        if v in distances:
            continue

        distances[v] = distance

        for u, weight in adj_list[v].items():
            vu_distance = distances[v] + weight
            if cutoff is not None:
                if vu_distance > cutoff:
                    continue
            if u in distances:

                if vu_distance < distances[u]:
                    raise ValueError

            elif u not in visited or vu_distance < visited[u]:
                visited[u] = vu_distance
                heappush(heap, (vu_distance, v, u))
                _update_paths(paths, u, v)
                predecessors[u] = [v]

            elif vu_distance == visited[u]:
                predecessors[u].append(v)
                _update_paths(paths, u, v)

    return paths, distances


def _update_paths(paths, u, v):
    paths[u] = []
    for path in paths[v]:
        paths[u] = paths[u] + [path + [u]]
