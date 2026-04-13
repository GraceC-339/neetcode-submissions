class Solution:
    def findMin(self, nums: List[int]) -> int:
        # use binary search to search 2 parts of the array

        res = nums[0] #the left number
        l, r = 0, len(nums)-1

        while l <= r:
            # if the array is already sorted, the min is the left num
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l+r)//2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m-1
            
        return res
            