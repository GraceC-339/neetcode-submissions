class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {} # number:index

        for idx, val in enumerate(nums): #=> (idx,val)
            if (target-val) in visited:
                return [visited[target-val],idx]
            visited[val] = idx
    
            