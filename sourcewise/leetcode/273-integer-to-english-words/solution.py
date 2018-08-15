class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        return self.convertToEnglish(num)

    def convertToEnglish(self, num):
        dictionary = {1: 'One',
                      2: 'Two',
                      3: 'Three',
                      4: 'Four',
                      5: 'Five',
                      6: 'Six',
                      7: 'Seven',
                      8: 'Eight',
                      9: 'Nine',
                      10:'Ten',
                      11:'Eleven',
                      12:'Twelve',
                      13:'Thirteen',
                      14:'Fourteen',
                      15:'Fifteen',
                      16:'Sixteen',
                      17:'Seventeen',
                      18:'Eighteen',
                      19:'Nineteen',
                      20:'Twenty',
                      30:'Thirty',
                      40:'Forty',
                      50:'Fifty',
                      60:'Sixty',
                      70:'Seventy',
                      80:'Eighty',
                      90:'Ninety'}
        if num >= 10**9:
            n = num/(10**9)
            return self.convertToEnglish(n) + ' ' + 'Billion' + ' ' + self.convertToEnglish(num%(10**9))
        elif num >=10**6:
            n = num/10**6
            return self.convertToEnglish(n) + ' ' + 'Million' + ' ' + self.convertToEnglish(num%(10**6))
        elif num >=10**3:
            n = num/10**3
            return self.convertToEnglish(n) + ' ' + 'Thousand' + ' ' + self.convertToEnglish(num % (10 ** 3))
        elif num >= 10**2:
            n = num/10**2
            return self.convertToEnglish(n) + ' ' + 'Hundred' + ' ' + self.convertToEnglish(num % (10 ** 2))
        elif num >= 20:
            return dictionary[num/10*10] + ' ' + self.convertToEnglish(num%10)
        elif num > 0:
            return dictionary[num]
        else:
            return ''

if __name__ == '__main__':
   pass