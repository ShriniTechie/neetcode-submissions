class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        
        # In Top K Frequent Elements, k means:
        # Return the k elements with the highest frequencies, not elements whose frequency is >= k.
        # # for key in freq:
        #     if freq[key] >= k:
        #         res.append(key)
        sorted_freq = sorted(freq, key = freq.get, reverse = True)
        return sorted_freq[:k]