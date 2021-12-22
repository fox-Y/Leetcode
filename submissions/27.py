class Solution(object):

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        len_nums = len(nums)
        i = 0
        j = len_nums-1
        
        while i<j:
            while (i<j and nums[i]!=val):
                i += 1
            while (i<j and nums[j]==val):
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        return i if nums[i] == val else i+1

nums, val = [0,1,2,2,3,0,4,2], 2
s = Solution()
n = s.removeElement(nums, val)
print(n)
print(nums)