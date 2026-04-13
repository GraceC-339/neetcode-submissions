class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_nums = set(nums)

        longest = 0

        for num in hash_nums:
            if (num-1) not in hash_nums:
                length = 1
                while (num+length) in hash_nums:
                    length += 1
                longest = max(length, longest)
        
        return longest
