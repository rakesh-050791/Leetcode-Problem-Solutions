# 1822. Sign of the Product of an Array


# There is a function signFunc(x) that returns:

# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.
# You are given an integer array nums. Let product be the product of all values in the array nums.

# Return signFunc(product).


# Example 1:

# Input: nums = [-1,-2,-3,-4,3,2,1]
# Output: 1
# Explanation: The product of all values in the array is 144, and signFunc(144) = 1
# Example 2:

# Input: nums = [1,5,0,2,-3]
# Output: 0
# Explanation: The product of all values in the array is 0, and signFunc(0) = 0
# Example 3:

# Input: nums = [-1,1,-1,1,-1]
# Output: -1
# Explanation: The product of all values in the array is -1, and signFunc(-1) = -1

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        result = 1

        for num in nums:
            if num == 0:
                return 0

            if num < 0:
                result =  -1 * result
        
        return result



# Time complexity: O(n) 

# Space complexity: O(1)



# Intution 

# keep track of the sign of the product while multiplying the numbers in nums.

# We initialize an integer variable sign = 1 to keep track of the product's sign.
# We flip sign to -1 * sign whenever we get a negative number while iterating nums. After iterating through all of the numbers, we return sign unless there is a 0 in nums, in which case the answer is 0.


