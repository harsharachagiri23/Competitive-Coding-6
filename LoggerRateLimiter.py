class Logger:
    
    def __init__(self):
        self.map = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        last = self.map.get(message)
        if last is None or timestamp - last >= 10:
            self.map[message] = timestamp
            return True 
        return False     









# Time Complexity: O(1)
# Space Complexity: O(M)
# Leetcode:  359
# Problem faced: Nothing
        



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)