'''
Implement atoi which converts a string to an integer.
'''

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        vec_int = []
        if len(str) <= 0:
            return (0)
        else:
            i = 0
            while i < len(str):
                if str.isspace(str[i]):
                    i += 1
                elif str[i] == '-' and len(x) == 0:
                    vec_int.append(str[i])
                else
