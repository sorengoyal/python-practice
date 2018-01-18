class Solution:
    class Complex:
        def __init__(self, r, i):
            self.real = r
            self.imag = i

        def __repr__(self):
            if self.imag < 0:
                return str(self.real) + str(self.imag) + 'i'
            else:
                return str(self.real) + '+' + str(self.imag) + 'i'

        def __mul__(self, other):
            r = self.real * other.real - self.imag * other.imag
            i = self.real * other.imag + self.imag * other.real
            return self.__init__(r, i)

    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c1 = self.parse(a)
        c2 = self.parse(b)
        print(c1)
        print(c1*c2)
        return (c1*c2).__repr__()

    def parse(self, c):
        i = 1
        while c[i].isdigit():
            i = i + 1
        r = int(c[:i])
        i = int(c[i:-1])
        return self.Complex(r,i)

if __name__ == '__main__':
    sln = Solution()
    print(sln.complexNumberMultiply("1+1i", "1-1i"))