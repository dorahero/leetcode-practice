class Solution:
    def reverseBits(self, n: int) -> int:
        n_bin_list = list(f"{n:032b}")
        n_bin_list.reverse()
        rn_bim = "".join(n_bin_list)
        return int(rn_bim, 2)

solution = Solution()
n = 2147483644
print(solution.reverseBits(n))