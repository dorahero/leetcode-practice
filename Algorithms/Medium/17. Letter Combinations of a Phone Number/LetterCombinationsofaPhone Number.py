class Solution(object):
    def letterCombinations(self, digits):
        dig_dict = {str(i): [3] for i in range(2, 10)}
        dig_dict['7'] = [4]
        dig_dict['9'] = [4]
        i = 97
        for d in dig_dict:
            for j in range(dig_dict[d][0]):
                dig_dict[d].append(chr(i))
                i += 1
        ans = []
        ans_dig = []
        for d in digits:
            ans_dig.append(dig_dict[d][1:])
        total_len = 1
        for x in ans_dig[1:]:
            total_len *= len(x)
        _ = 1
        for j, x in enumerate(ans_dig):
            for i, y in enumerate(x):
                if j == 0:
                    for a in range(int(total_len)):
                        ans.append(y)
                else:
                    for r in range(_):
                        for b in range(int(total_len) // len(x)):
                            ans[i*(int(total_len) // len(x))+b+r*int(total_len)] += y
            if j > 0:
                total_len = total_len / len(x)
            _ *= len(x)

        return ans

if __name__=="__main__":
    res = Solution().letterCombinations("23")
    print(res)