# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         freq = {}
#         for num in nums:
#             freq[num] = freq.get(num, 0) + 1
#             # if num not in freq:
#             #     freq[num] = 0
#             # freq[num] += 1
        
#         # In Top K Frequent Elements, k means:
#         # Return the k elements with the highest frequencies, not elements whose frequency is >= k.
#         # # for key in freq:
#         #     if freq[key] >= k:
#         #         res.append(key)
#         sorted_freq = sorted(freq, key = freq.get, reverse = True)
#         return sorted_freq[:k]

# Using bucket sort usage! 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        # Count frequency
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Create buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        # Put numbers into bucket based on frequency
        for num, count in freq.items():
            buckets[count].append(num)

        # Get top k frequent elements
        res = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)

                if len(res) == k:
                    return res

        return res