'''
Given two strings s and t , write a function to determine if t is an anagram of s.
'''

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        hash_table = {}

        for i in range(len(s)):
            if s[i] in hash_table:
                hash_table[s[i]] += 1
            else:
                hash_table[s[i]] = 1

        for j in range(len(t)):
            if t[j] in hash_table:
                hash_table[t[j]] -= 1
                if hash_table[t[j]] < 0:
                    return False
            else:
                return False

        if sum(hash_table.values()) > 0:
            return False
        else:
            return True

s = "rat"
t = "car"
test = Solution()

print(test.isAnagram(s,t))