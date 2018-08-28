from collections import Counter


class Popular:
    def __init__(self):
        self._popular_calc = Counter(ele for data in self.dataset for ele in data).most_common()

    def popular(self, data, n=None):
        return [(ele, freq) for ele, freq in self._popular_calc if ele not in data][:n]
