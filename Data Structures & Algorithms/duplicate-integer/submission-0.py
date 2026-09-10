class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter 
        freq = Counter(nums)

        for key in freq:
            if freq[key] > 1:
                return True 
        return False
        