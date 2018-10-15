'''
Write a function that takes a string as input and returns the string reversed.
'''

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        temp = []
        for i in range(len(s)):
            temp.append(s[len(s) - 1 - i])

        return (''.join(temp))

x = "A man, a plan, a canal: Panama"

test = Solution()

print(test.reverseString(x))