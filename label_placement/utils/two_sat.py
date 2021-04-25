from typing import List, Dict

from .graph import get_all_nodes, find_scc


def solve_two_sat(implication_graph: Dict[str, List[str]]) -> Dict[str, bool]:
    variables = get_all_nodes(implication_graph)
    variables = set(map(lambda x: x.replace('!', ''), variables))

    scc = find_scc(implication_graph)

    solution = dict()
    for var in variables:
        neg_var = f'!{var}'
        if scc[var] == scc[neg_var]:
            return None # no solution
        solution[var] = True if scc[var] > scc[neg_var] else False
    
    return solution
