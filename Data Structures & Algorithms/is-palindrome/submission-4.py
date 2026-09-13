class Solution:
    def isPalindrome(self, s: str) -> bool:
        # raw_string = ""
        # for char in s:
        #     if char.isalnum():
        #         raw_string += char 
        # Since, storing raw_string requires O(n) space complexity
        # raw_string = "".join(
        #     [char.lower() for char in s if char.isalnum()]
        # )

        # left = 0
        # right = len(raw_string)-1
        # raw_string = raw_string.lower()

        # while left < right:
        #     if raw_string[left] != raw_string[right]:
        #         return False
        #     left += 1
        #     right -= 1

        # return True  
        
        # O(1) - space complexity
        left = 0
        right = len(s)-1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1 
        return True  
        

