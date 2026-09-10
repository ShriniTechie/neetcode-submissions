class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(nums):
            complement = target - num 
            if complement in seen:
                return [seen[complement], index]
            seen[num] = index
        return []
        
        # Following logic will not  work for unsorted array
        # If you sort the array, it will change the indexs
        # nums = sorted(nums)
        # left = 0
        # right = len(nums) - 1

        # while left < right:
        #     total = nums[left] + nums[right]
        #     if total == target:
        #         return [left, right]
        #     elif total < target:
        #         left += 1
        #     else:
        #         right -= 1
        # return []
        