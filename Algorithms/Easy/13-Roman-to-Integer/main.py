class Solution(object):
    def romanToInt(self, s):
        dict_I = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        dict_X = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        a = []
        for d in dict_X:
            if d in s:
                a.append(dict_X[d])
                s = s.replace(d, '')
        for t in s:
            a.append(dict_I[t])
        return sum(a)

solution = Solution()
result = solution.romanToInt('IV')
print(result)  

