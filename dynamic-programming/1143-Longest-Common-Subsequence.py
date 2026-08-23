# Problem: https://leetcode.com/problems/longest-common-subsequence/
# Approach: Use dp grid of length m + 1 and n + 1 where m and n are length of the two input texts. Starting from grid[1][1] (skipping dummy row and col of all 0s),
#           if the two chars match at that index (each index representing a comparison of two chars in text1 and text2), add 1 to the top left diagonal,
#           diagonal because that represents the lcs before the two chars currently being compared were added on. Otherwise take the max of the up and left directions in the dp so we keep the max lcs that we know at that point.
# Complexity: O(r * c) time, O(c * r) space where r is num of rows and c is num of cols

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        
        # extra row and col to help fill matrix
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[-1][-1]
