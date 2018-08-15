from random import random
from functools import reduce

class Codec:
    def __init__(self):
        self.db = {}
        self.chars = [chr(ord('a') + i) for i in range(0,26)] + [chr(ord('A') + i) for i in range(0,26)]

    def generateRandomString(self):
        l = [self.chars[int(random()*52)] for i in range(8)]
        return reduce(lambda acc, ch:acc+ch, l)

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        url = "http://tinyurl.com/" + self.generateRandomString()
        while url in self.db:
            url = "http://tinyurl.com/" + self.generateRandomString()

        self.db[url] = longUrl
        return url

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.db[shortUrl]

if __name__ == '__main__':
    # Your Codec object will be instantiated and called as such:
    codec = Codec()
    print(codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl")))