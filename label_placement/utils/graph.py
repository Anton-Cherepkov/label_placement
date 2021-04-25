from collections import defaultdict
from typing import Dict


def get_all_nodes(graph):
    nodes = set()
    for k, v in graph.items():
        nodes.update([k,] + v)
    return nodes


def get_transposed_graph(graph):
    transposed_graph = defaultdict(list)
    for from_, to_list in graph.items():
        for to in to_list:
            transposed_graph[to].append(from_)
    return transposed_graph


def topological_sort_impl(graph, node, visited, order):
    visited[node] = True
    for next_node in graph[node]:
        if not visited[next_node]:
            topological_sort_impl(graph, next_node, visited, order)
    order.append(node)


def topological_sort(graph):
    nodes = get_all_nodes(graph)
    
    visited = defaultdict(bool)
    order = list()
    for node in nodes:
        if not visited[node]:
            topological_sort_impl(graph, node, visited, order)
    
    assert len(order) == len(nodes)
    return list(reversed(order))


def find_scc_impl(graph, node, component_ix, curr_component_ix):
    component_ix[node] = curr_component_ix
    for next_node in graph[node]:
        if component_ix[next_node] is None:
            find_scc_impl(graph, next_node, component_ix, curr_component_ix)


def find_scc(graph) -> Dict[str, int]:
    order = topological_sort(graph)
    graph_transposed = get_transposed_graph(graph)

    component_ix = defaultdict(lambda: None)

    curr_component_ix = 0
    for node in order:
        if component_ix[node] is None:
            find_scc_impl(graph_transposed, node, component_ix, curr_component_ix)
            curr_component_ix += 1

    assert len(component_ix) == len(order)
    return component_ix
