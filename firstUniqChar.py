'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
'''

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        hash_table = {}
        for i in range(len(s)):
            if s[i] in hash_table:
                hash_table[s[i]] += 1
            else:
                hash_table[s[i]] = 1

        for i in range(len(s)):
            if hash_table[s[i]] == 1:
                return (i)

        return (-1)

s = "loveleetcode"
test = Solution()

print(test.firstUniqChar(s))