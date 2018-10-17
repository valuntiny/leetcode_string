'''
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if len(needle) == 0:
            return (0)
        else:
            for i in range(0, len(haystack) - len(needle) + 1):
                if haystack[i:(i + len(needle))] == needle:
                    return (i)
            return (-1)

haystack = "aaaaa"
needle = "bba"

test = Solution()
print(test.strStr(haystack, needle))