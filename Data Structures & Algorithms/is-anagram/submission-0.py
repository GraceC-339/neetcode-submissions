class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #brute force
        #loop through each string and compare
        # count how many letters there are 
        # i have no clueee

        # sort each string and see if they're the same
        #1.

        sorted_s = ''.join(sorted(s))
        sorted_t = ''.join(sorted(t))

        return sorted_s == sorted_t
     
