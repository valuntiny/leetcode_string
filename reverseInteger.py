'''
Given a 32-bit signed integer, reverse digits of an integer.
'''

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        s = (x > 0) - (x < 0)
        x = int(str(abs(x))[::-1]) * s

        return (x * (x < 2 ** 31) * (x >= - 2 ** 31))


x = -123
test = Solution()

print(test.reverse(x))