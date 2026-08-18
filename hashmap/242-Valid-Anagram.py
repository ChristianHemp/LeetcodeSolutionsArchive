# Problem: https://leetcode.com/problems/valid-anagram/
# Approach: Maintain frequency hashmap for all chars in string s, decrement frequencies iterating through string t which should result in all 0s to return True, else return False
# Complexity: O(n) time, O(k) space where k is the number of distinct chars in s

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash_map = {}

        for char in s:
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1
        
        for char in t:
            if char not in hash_map:
                return False

            hash_map[char] -= 1
            
            if(hash_map[char] < 0):
                return False

        return True
