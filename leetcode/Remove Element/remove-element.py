class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        """Pseudocode
        we have nums and val using two pointers
        start at 1 = 0
        loop through the array
        for num in nums:
            if j!= val
            copy nums j to nums i  
            move i forward
            """
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i+=1
        return i