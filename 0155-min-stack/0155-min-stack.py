import heapq
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_val = self.getMin()
        if min_val == None or min_val > val:
            min_val = val
        self.stack.append([val, min_val])

    def pop(self) -> None:
        if len(self.stack) == 0: return None

        val, _ = self.stack.pop()
        return val

    def top(self) -> int:
        if len(self.stack) == 0: return None

        val, _ = self.stack[-1]
        return val

    def getMin(self) -> int:
        if len(self.stack) == 0: return None

        _, min_val = self.stack[-1]
        return min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()