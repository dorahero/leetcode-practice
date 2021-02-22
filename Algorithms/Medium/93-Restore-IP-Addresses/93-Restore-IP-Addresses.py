class Solution(object):
    def restoreIpAddresses(self, s):
        ans = []
        k = 0
        self.backtrack(s,ans,k,'')
        return ans



    def backtrack(self, s, ans,k, temp=''):
        if k==4 and len(s)==0:
            # if get 4 numbers
            ans.append(temp[:-1])
            return
        if k==4 or len(s)==0:
            # if get 4 numbers for IP, but still remain some numbers unused
            # or all number be used, but not get 4 number for IP 
            return

        for i in range(3):
            if k>4 or i+1>len(s):
                break

            if int(s[:i+1])>255:
                continue
            # if the number is start with 0 and not '0'
            if i != 0 and s[0]=='0':
                continue
            # remain string, ans, checker, temp IP
            self.backtrack(s[i+1:], ans, k+1, temp+s[:i+1]+'.')

if __name__ == '__main__':
    res = Solution().restoreIpAddresses(s = "101023")
    print(res)  