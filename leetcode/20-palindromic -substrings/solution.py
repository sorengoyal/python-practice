class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count = 0
        for i in range(0,n):
            for j in range(i,n+1):
                #print(j,end=' ')
                if self.isPalindrome(s[i:j]):
                    count += 1
        return count

    def isPalindrome(self,s):
        if len(s) == 0:
            return False
        m = int(len(s)/2)
        for i in range(0,m):
            if s[i] != s[-1-i]:
                return False
        return True
if __name__ == '__main__':
    sln = Solution()
    print(sln.countSubstrings('aabc'))