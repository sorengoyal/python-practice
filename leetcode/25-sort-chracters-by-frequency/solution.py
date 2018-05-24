from functools import reduce
class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        charmap = {}
        for c in s:
            if c not in charmap:
                charmap[c] = 1
            else:
                charmap[c]+= 1
        pairs = [tuple([k, charmap[k]]) for k in charmap]
        return reduce(lambda sum, p: sum+(p[1]*p[0]), sorted(pairs, key=lambda p: p[1],reverse=True), "")


if __name__ == '__main__':
    sln = Solution()
    print(sln.frequencySort("Aabb"))