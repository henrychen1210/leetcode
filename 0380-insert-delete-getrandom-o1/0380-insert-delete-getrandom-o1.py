import random

class RandomizedSet:

    def __init__(self):
        self.array = []
        self.idx_map = {}

    def insert(self, val: int) -> bool:
        if val in self.idx_map:
            return False
        self.array.append(val)
        self.idx_map[val] = len(self.array) - 1

    def remove(self, val: int) -> bool:
        if val not in self.idx_map:
            return False
        idx = self.idx_map[val]
        self.array[idx] = self.array[-1]
        self.idx_map[self.array[-1]] = idx
        self.array.pop()
        del self.idx_map[val]
        return True

    def getRandom(self) -> int:
        idx = random.randrange(0, len(self.array))
        return self.array[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()