class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check the frequency of the letter
        # only lowercase

   

        # use comprehension
        s_freq = {k:s.count(k) for k in s}
        t_freq = {k:t.count(k) for k in t}

        return s_freq == t_freq

