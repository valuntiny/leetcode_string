'''
Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
'''

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        result = "1"    # store the result

        i = 1   # counter for index
        while i < n:
            count_n = 1  # occurrence
            count_key = result[0]  # key-value
            temp = []

            j = 1   # counter for the array traverse loop
            while j < (len(result)):
                if result[j] == result[j - 1]:
                    count_n += 1
                else:
                    temp.append(str(count_n))    # output
                    temp.append(count_key)
                    count_n = 1
                    count_key = result[j]
                j += 1
            temp.append(str(count_n))    # deal with the last item
            temp.append(count_key)
            result = ''.join(temp)  # every item in temp shall be string type
            i += 1

        return (result)

test = Solution()
print(test.countAndSay(8))
