
from connected import connected_components
from connected import number_connected_components
from betweenness import get_edges_with_highest_betweenness as get_edges_with_highest_betweenness


def girvan_newman(graph, level):

    comp = girvan_newman_generator(graph)

    for c in comp:
        if len(c) == level:
            return c


def girvan_newman_generator(graph):

    if graph.number_of_edges() == 0:
        yield tuple(connected_components(graph))
        return

    _graph = graph.copy()
    _remove_self_loops(_graph)

    while _graph.number_of_edges() > 0:
        yield _without_highest_betweenness_edge(_graph)


def _without_highest_betweenness_edge(graph):
    original_num_components = number_connected_components(graph)
    num_connected_components = original_num_components

    while num_connected_components <= original_num_components:

        edge = get_edges_with_highest_betweenness(graph)[0]
        graph.remove_edge(*edge)

        new_components = tuple(connected_components(graph))
        num_connected_components = len(new_components)

    return new_components


def _remove_self_loops(graph):
    for n, neighbors in graph.adj_list.items():
        if n in neighbors:
            graph.remove_edge(n, n)