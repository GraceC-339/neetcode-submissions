class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = defaultdict(int)

        for n in nums:
            res[n] += 1
        
        top_k = sorted(res, key=res.get, reverse= True)[:k]

        return top_k
