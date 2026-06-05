class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {
            ')':'(',
            '}':'{',
            ']':'[' 
        }

        stack =[]

        for char in s:
            if char not in brackets:
                stack.append(char)
            else:
                if not stack:
                    return False

                top = stack.pop()

                if top!= brackets[char]:
                    return False

        return len(stack) == 0