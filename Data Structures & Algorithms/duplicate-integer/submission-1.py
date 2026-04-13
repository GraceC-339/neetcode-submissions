class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Brute Force , O(n^2),O(1) - no need for extra memory
        # Sorting-> compare the next num, O(nlogn), O(1)
        # Hashset

        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            
            hashset.add(n)
        
        return False
