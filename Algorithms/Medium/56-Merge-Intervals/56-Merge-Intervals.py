class Solution(object):
    def merge(self, intervals):
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        print(intervals)
        ans = []
        x, y = intervals[0]
        for i, j in enumerate(intervals[1:]):
            print(x,y)
            if y < j[0]:
                if [x, y] not in ans:
                    ans.append([x,y])
                if i == len(intervals)-2:
                    ans.append(j)
                x, y = j
            else:
                y = max(y,j[1])
                x = min(x, j[0])
                if i == len(intervals)-2:
                    ans.append([x,y])

        return ans

if __name__ == '__main__':
    res = Solution().merge([[1,3],[2,6],[8,10],[15,18]])
    print(res)  