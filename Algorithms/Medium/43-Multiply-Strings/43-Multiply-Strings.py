class Solution(object):
    def multiply(self, num1, num2):
        a = int(num1)
        b = int(num2)
        return str(a*b)
if __name__ == "__main__":
    res = Solution().multiply("123", "456")
    print(res)