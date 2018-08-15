class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        lp = self.constructVector(licensePlate)
        minindex = 0
        minvalue = 100
        for i in range(len(words)):
            count = 0
            v = self.constructVector(words[i])
            for lpc,vc in zip(lp, v):
                if vc - lpc < 0:
                    count = 100
                    break
                count += vc - lpc
            if count == 0:
                return words[i]
            if minvalue > count:
                minvalue = count
                minindex = i
        return words[minindex]

    def constructVector(self, word):
        v = [0]*26
        for ch in word:
            index = ord(ch.lower()) - ord('a')
            if 0 <= index and index <=26:
                v[index] += 1
        return v

if __name__ == '__main__':
    sln = Solution()
    licensePlate = "1s3 456"
    words = ["looks", "pest", "stew", "show"]
    print(sln.shortestCompletingWord(licensePlate, words))

