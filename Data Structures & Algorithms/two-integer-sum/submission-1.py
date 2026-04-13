class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # nums[i]
        # the other number is target-nums[i]

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        
        # use hash map - need to check if target-nums[i] exists
        # map the value to the index
        # only need to iterate the array once

        prevMap = {} # val:index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        
        # i is the index, n is the value/number


        