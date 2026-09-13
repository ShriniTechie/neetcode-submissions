class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        
        for num in nums_set:
            if num-1 not in nums_set:
                # Starting the fresh sequence 
                current = num
                current_len = 1

                while current + 1 in nums_set:
                    current += 1
                    current_len += 1

                max_len = max(max_len, current_len)
        
        return max_len

            
