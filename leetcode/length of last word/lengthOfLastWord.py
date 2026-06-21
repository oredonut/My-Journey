class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int

        Pseudocode
        start from the last index
        if the current index is not a space move left
        loop from the back till the next space
        return the count
        """

        i = s.split() 
        return len(i[-1])
        
