class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1
        
        res = []

        while k > 0:
            max_num = max(freq, key = freq.get)
            res.append(max_num)
            freq.pop(max_num)
            k -= 1
        
        return res
        
