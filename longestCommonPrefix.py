'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ("")
        elif len(strs) == 1:
            return (strs[0])
        else:
            lcp = []    # longest common prefix
            for i in range(len(strs[0])):   # vertical scanning
                ref = strs[0][i]    # take str0 as reference
                for j in range(1, len(strs)):
                    if len(strs[j]) <= i:
                        return (''.join(lcp))
                    elif strs[j][i] != ref:
                        return (''.join(lcp))

                lcp.append(ref)

            return (''.join(lcp))


x = ["dog","racecar","car"]
test = Solution()

print(test.longestCommonPrefix(x))