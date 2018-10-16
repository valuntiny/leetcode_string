'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.
'''

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        i = 0
        j = len(s) - 1
        str_left = ""
        str_right = ""
        while i < j:
            if (not str.isalnum(s[i])):
                i += 1
            elif (not str.isalnum(s[j])):
                j -= 1
            else:
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1

        return True

x = "race a car"
test = Solution()

print(test.isPalindrome(x))