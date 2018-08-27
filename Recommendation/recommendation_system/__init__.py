from .most_popular import Popular
from .user_based import UserBased
from .item_based import ItemBased


class Recommender(Popular, UserBased, ItemBased):
    def __init__(self, dataset):
        self.dataset = dataset

        Popular.__init__(self)
        UserBased.__init__(self)
        ItemBased.__init__(self)
