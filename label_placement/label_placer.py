from typing import List
from copy import deepcopy
from collections import defaultdict

from .label import Label
from .utils.general import label_to_bbox, has_intersection
from .utils.two_sat import solve_two_sat


def find_placement(possible_labels: List[List[Label]]):
    assert max(map(len, possible_labels)) <= 2, 'Maximum 2 positions are possible for every label'
    possible_labels = deepcopy(possible_labels)

    # Add fake possible label if only one is specified
    for labels in possible_labels:
        if len(labels) == 1:
            labels.append(labels[0])

    # labels -> bboxes
    possible_bboxes = []
    for labels in possible_labels:
        possible_bboxes.append(list(map(label_to_bbox, labels)))

    formula = list()
    implication_graph = defaultdict(list)

    # find pairwise intersections
    for label_ix, bboxes in enumerate(possible_bboxes):
        for i, bbox in enumerate(bboxes):
            for label_prime_ix, bboxes_prime in enumerate(possible_bboxes):
                if label_prime_ix == label_ix:
                    continue
                for j, bbox_prime in enumerate(bboxes_prime):
                    if has_intersection(bbox, bbox_prime):
                        sat_var_impl_from = f"{'!' if i == 0 else ''}x{label_ix}"
                        sat_var_impl_to = f"{'!' if j == 1 else ''}x{label_prime_ix}"
                        formula.append(f"({sat_var_impl_from} -> {sat_var_impl_to})")
                        implication_graph[sat_var_impl_from].append(sat_var_impl_to)
    
    formula = " & ".join(formula)
    print(formula)

    # Solve 2-SAT
    sat_solution = solve_two_sat(implication_graph)
    if sat_solution is None:
        return None
    
    # Choose final labels
    labels_solution = []
    for ix, labels in enumerate(possible_labels):
        try:
            labels_solution.append(labels[int(sat_solution[f"x{ix}"])])
        except KeyError:
            labels_solution.append(labels[0])
    
    return labels_solution
