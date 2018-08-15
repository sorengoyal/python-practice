class TidyNumbers:

    def findTidyNumber(self, N, k):

        if len(digits) == 1:
            if digits[0] == 0:
                return [9]
            else:
                return digits
        T_ = self.findTidyNumber(N, k-1)

        t = 9
        while (int(N[:k]) - 10*int(T_) - t) < 0:
            t -= 1
            if t < int(N[k-1]):
                break
        return T_ + str(t)






if __name__ == '__main__':
    sln = TidyNumbers()
    sln.findTidyNumber(sln.disintegrate(132))
    sln.findTidyNumber(sln.disintegrate(1000))
    sln.findTidyNumber(sln.disintegrate(7))
    sln.findTidyNumber(sln.disintegrate(111111111111111110))