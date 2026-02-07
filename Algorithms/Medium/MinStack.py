class MinStack:

    def __init__(self):
        self.nums = []

    def push(self, val: int) -> None:
        self.nums.append(val)

    def pop(self) -> None:
        self.nums.pop()

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return min(self.nums)
        


# Your MinStack object will be instantiated and called as such:

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.nums)
print(minStack.getMin())
minStack.pop()
print(minStack.nums)
print(minStack.top())
print(minStack.getMin())