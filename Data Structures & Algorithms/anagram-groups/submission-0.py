class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list) #mapping the character count to the list of anagrams

        for s in strs:
            count = [0] * 26 #a...Z

            for c in s:
                count[ord(c) - ord("a")] += 1  #use ascii value to caculate the index\

            res[tuple(count)].append(s)
        
        return res.values()