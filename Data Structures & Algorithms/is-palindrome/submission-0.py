class Solution:
    def isPalindrome(self, s: str) -> bool:
        # case - insensitive => turn all of them to lowercase
        # ignore all non-alphanumeric characters - delete the blank spaces and marks
        # use function .isalnum()

        newStr = ''

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        
        return newStr == newStr[::-1]


