class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # loop through the array and fine the matched one

        for i in range(len(nums)):
            if nums[i] == target:
                return i
        
        return -1