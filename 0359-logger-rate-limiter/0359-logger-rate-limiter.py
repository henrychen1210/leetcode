class Logger:

    def __init__(self):
        self.memo = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        print(self.memo)
        if (message in self.memo and timestamp >= self.memo[message]) or (message not in self.memo):
            self.memo[message] = timestamp + 10
            return True
        return False
        

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)