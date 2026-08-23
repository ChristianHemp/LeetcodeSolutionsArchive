# Problem: https://leetcode.com/problems/top-k-frequent-elements/
# Approach: Use a hashmap to count frequencies of elements in nums. Use an array of lists where index is counts and value is element that has that many counts. 
#           Iterate through frequencies from end to start appending the elements to res until its length is k.
# Complexity: O(n) time, O(n) space

from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        frequencies = [[] for _ in range(len(nums) + 1)]
        res = []
        
        for num in nums:
            counts[num] += 1
        
        for key, val in counts.items():
            frequencies[val].append(key)
        
        for i in range(len(frequencies) - 1, 0, -1):
            for element in frequencies[i]:
                res.append(element)
                if len(res) == k:
                    return res
