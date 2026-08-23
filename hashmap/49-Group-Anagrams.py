# Problem: https://leetcode.com/problems/group-anagrams/
# Approach: Use a defaultdict to store a lists of anagrams with a tuple of length 26 containing the counts of each char as the key.
#           ord() for ascii/unicode values, 'a' starts at 97, so for 0 index subtract ord('a') from each value to get 1 index. return list of defaultdict values.
# Complexity: O(n) time, O(n) space

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for s in strs:
            counts = [0] * 26

            for c in s:
                counts[ord(c) - ord('a')] += 1
            
            hm[tuple(counts)].append(s)
        
        return list(hm.values())
