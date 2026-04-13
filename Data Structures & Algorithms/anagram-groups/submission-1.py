class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorting

        res = defaultdict(list) # => {sorteS : ['','']}

        for str in strs:
            sortedS = ''.join(sorted(str))
            res[sortedS].append(str)
        
        return list(res.values())