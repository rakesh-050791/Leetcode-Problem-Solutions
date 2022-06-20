# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward.

# For example, 121 is a palindrome while 123 is not.
 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

class Solution:
    def isPalindrome(self, x: int) -> bool:        
        if x < 0:
            return False
        
        refNum = self.reverse(x)
            
        return refNum == x
    
    def reverse(self, x: int):
        reverse = 0 
        
        while x > 0:
            remainder = x % 10 
            
            reverse = (reverse * 10) + remainder 
            
            x = x // 10
            
        return reverse
        