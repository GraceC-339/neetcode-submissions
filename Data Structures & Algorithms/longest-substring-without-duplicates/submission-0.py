class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()

        # sliding window
        l = 0
        res = 0

        # use for loop, r pointer to go through each char
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res
