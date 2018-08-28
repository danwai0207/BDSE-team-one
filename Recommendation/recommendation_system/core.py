import math
from collections import defaultdict


def dot(p, q):
    return sum(map(lambda p_i, q_i: p_i * q_i, p, q))


def similarity_calc(p, q):
    return dot(p, q) / math.sqrt(dot(p, p) * dot(q, q))


class CollaborativeFiltering:
    def __init__(self):
        self.unique = sorted(tuple({ele for data in self.dataset for ele in data}))
        self.usr_matrix = [[similarity_calc(p, q) for q in self._usr_item_map()] for p in self._usr_item_map()]

    def _usr_item_vec(self, data):
        return [1 if ele in data else 0 for ele in self.unique]

    def _usr_item_map(self):
        return map(self._usr_item_vec, self.dataset)
