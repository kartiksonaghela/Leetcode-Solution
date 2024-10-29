class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:  # Handle empty string case
            return ""

        final_result = []
        
        # Generate all possible substrings
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                # Check if the substring is a palindrome
                if substring == substring[::-1]:
                    final_result.append(substring)

        # Find and return the longest palindromic substring
        return max(final_result, key=len, default="") 