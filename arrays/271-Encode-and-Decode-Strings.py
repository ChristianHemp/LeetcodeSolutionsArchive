# Problem: https://leetcode.com/problems/encode-and-decode-strings/
# Approach: Build an encoded string that contains the length of each string followed by a '%' character joined together. To decode find the % characters to get the length of the string and read the chars for _ in range(length)
# Complexity: O(n) time, O(n) space

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_strs = []

        for s in strs:
            encoded_strs.append(f"{len(s)}%{s}")
        
        return ''.join(encoded_strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        j = 0
        while i < len(s):
            while s[j] != '%':
                j += 1
            
            length = int(s[i:j])
            chars = []

            for _ in range(length):
                j += 1
                chars.append(s[j])
            
            res.append(''.join(chars))
            j += 1
            i = j
        
        return res
