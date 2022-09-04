
import os
import sys
import config as cfg
from parser import parse, get_headers
from girvan_newman import girvan_newman
from visualiser import draw

DEFAULT_EDGES_FILE = os.path.join(cfg.BASE_DIR, "data", "girvan_graph.csv")

if __name__ == '__main__':

    edges_path = DEFAULT_EDGES_FILE if len(sys.argv) < 2 else sys.argv[1]

    source_header, target_header, weight_header = get_headers(edges_path)

    graph = parse(edges_path, edge_limit=cfg.EDGES_LIMIT,
                  source_header=source_header, target_header=target_header, weight_header=weight_header)

    number_of_edges = len(list(graph.edges))

    components = girvan_newman(graph, cfg.COMPONENTS_LEVEL)
    if cfg.DRAW:
        draw(graph, components)


