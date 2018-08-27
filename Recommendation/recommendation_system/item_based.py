from .core import *


class ItemBased(CollaborativeFiltering):
    def __init__(self):
        CollaborativeFiltering.__init__(self)
        item_matrix = [[vector[i] for vector in self._usr_item_map()] for i in range(len(self.unique))]
        self.item_matrix = [[similarity_calc(p, q) for q in item_matrix] for p in item_matrix]

    def most_similar_item_to(self, item_id):
        similar_vec = self.item_matrix[item_id]
        pairs = []
        for other_item, similarity in enumerate(similar_vec):
            if item_id != other_item and similarity > 0:
                pairs += [(self.unique[other_item], similarity)]

        return sorted(pairs, key=lambda x: x[1], reverse=1)

    def item_based(self, subset, include_current_items=False):
        suggestions = defaultdict(float)
        sub_set = [vec for vec in self._usr_item_map()][subset]
        for item_id, is_true in enumerate(sub_set):
            if is_true:
                similar_items = self.most_similar_item_to(item_id)
                for item, similarity in similar_items:
                    suggestions[item] += similarity  # cumulative similarity

        suggestions = sorted(suggestions.items(), key=lambda x: x[-1], reverse=1)

        if include_current_items:
            return suggestions

        else:
            return [(suggestion, weight)
                    for suggestion, weight in suggestions
                    if suggestion not in self.dataset[subset]]
