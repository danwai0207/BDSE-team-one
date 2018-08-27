from .core import *


class UserBased(CollaborativeFiltering):
    def __init__(self):
        CollaborativeFiltering.__init__(self)

    def most_similar_set_to(self, subset):
        pairs = []
        for other_set, similarity in enumerate(self.usr_matrix[subset]):
            if subset != other_set and similarity > 0:  # find other users
                pairs += [(other_set, similarity)]  # with nonzero similarity

        return sorted(pairs,  # sort them by most similar
                      key=lambda x: x[-1], reverse=True)

    def user_based(self, subset, include_current_items=False):
        # sum up the similarities
        suggestions = defaultdict(float)
        for other_set, similarity in self.most_similar_set_to(subset):
            for ele in self.dataset[other_set]:
                suggestions[ele] = similarity

        # convert them to a sorted list
        suggestions = sorted(suggestions.items(), key=lambda x: x[-1], reverse=True)

        # and (maybe) exclude already-interests
        if include_current_items:
            return suggestions

        else:
            return [(suggestion, weight)  # filtering the suggestion already had
                    for suggestion, weight in suggestions if suggestion not in self.dataset[subset]]

