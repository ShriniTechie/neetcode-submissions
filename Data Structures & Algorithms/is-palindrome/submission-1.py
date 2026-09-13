class Solution:
    def isPalindrome(self, s: str) -> bool:
        raw_string = ""
        for char in s:
            if char.isalnum():
                raw_string += char 

        left = 0
        right = len(raw_string)-1
        raw_string = raw_string.lower()

        while left < right:
            if raw_string[left] != raw_string[right]:
                return False
            left += 1
            right -= 1

        return True  
        