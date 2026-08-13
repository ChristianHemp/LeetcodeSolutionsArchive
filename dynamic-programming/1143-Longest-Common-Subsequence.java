// Problem: https://leetcode.com/problems/longest-common-subsequence/
// Approach: 2D dynamic programming that stores the longest common subsequence for the prefixes both given strings
// Complexity: O(n * m) time, O(n * m) space

class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int n = text1.length();
        int m = text2.length();

        int[][] matrix = new int[n + 1][m + 1];

        for(int i = 1; i <= n; i++) {
            for(int j = 1; j <= m; j++) {
                if(text1.charAt(i - 1) == text2.charAt(j - 1)) {
                    matrix[i][j] = 1 + matrix[i - 1][j - 1];
                } else {
                    matrix[i][j] = Math.max(matrix[i - 1][j], matrix[i][j - 1]);
                }
            }
        }
        return matrix[n][m];
    }
}
