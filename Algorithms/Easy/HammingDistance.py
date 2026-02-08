class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_bin = f"{x:b}"
        y_bin = f"{y:b}"
        n = max(len(x_bin), len(y_bin))

        x_bin = f"{x:0{n}b}"
        y_bin = f"{y:0{n}b}"
        cnt = 0
        for i in range(n):
            if x_bin[i] != y_bin[i]:
                cnt += 1
        return cnt


solution = Solution()
x = 1
y = 4
print(solution.hammingDistance(x, y))