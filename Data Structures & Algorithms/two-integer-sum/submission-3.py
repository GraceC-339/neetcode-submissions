class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {} # number:index

        for idx, val in enumerate(nums): #=> (idx,val)
            diff = target - val
            if diff in visited:
                return [visited[diff],idx]
            visited[val] = idx
    
            