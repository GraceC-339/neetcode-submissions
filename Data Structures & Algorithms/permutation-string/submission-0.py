class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # count the freq of each char in s1
        count1 = {}

        for char in s1:
            count1[char] = 1 + count1.get(char,0)
        
        # sliding window for possible substring with the length of s1
        l = 0
        r = len(s1)-1

        while r < len(s2):
            count_sub = {}
            for c in range(l,r+1):
                count_sub[s2[c]] = 1 + count_sub.get(s2[c],0)
            if count_sub == count1:
                return True

            l += 1
            r += 1

        return False
            

        



