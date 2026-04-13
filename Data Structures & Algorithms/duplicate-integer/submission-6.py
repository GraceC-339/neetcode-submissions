class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums_set = set(nums)
        # return False if len(nums) == len(nums_set) else True
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False