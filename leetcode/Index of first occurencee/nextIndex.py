class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        Pseudocode
        start at i
        loop through haystack 
        if needle in haystack
        return the index
        if needle is not in haystack 
        return  -1 
        """

        for i in range(len(haystack) - len(needle) +1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

         