# 409-Longest Palindrome  #Greedy #Plaindrome #Strings


# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

# Constraints:

# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.


class Solution:
    def longestPalindrome(self, s: str) -> int:
        palindromeLength = 0

        charsCount = {}

        for char in s:
            if char in charsCount:
                charsCount[char] += 1
            else:
                charsCount[char] = 1

        
        for char in charsCount:
            if charsCount[char] % 2 == 0:
                palindromeLength += charsCount[char]
            else:
                palindromeLength += (charsCount[char] - 1)

        
        return palindromeLength + 1 if len(s) > palindromeLength else palindromeLength

# Video references 

# https://www.youtube.com/watch?v=J_Di2LmeLBQ

# https://www.youtube.com/watch?v=OISSoMogR5M


