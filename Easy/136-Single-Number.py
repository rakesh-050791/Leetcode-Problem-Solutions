# 136. Single Number

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.


# Note ** This can also be solved using hashmap or simply using loop and storing numbers in an array but that won't be optimal.


# Approach 1 : using XOR 

class Solution:
    def singleNumber(self, nums):
    	result = 0
    	for num in nums:
    		result ^= num 

    	return result


# Explanation:

# The XOR operation has the property that if you XOR a number with itself, the result is 0.

# If we XOR all elements in the array where each element appears twice, the XOR of those elements will be 0 because the pairs cancel each other out.

# The element that appears only once will remain in the result because there is no corresponding pair to cancel it out.
# For the given example [2, 2, 1]:

# 2 ^ 2 ^ 1 is equivalent to 0 ^ 1, which is 1.

# This solution has a linear runtime complexity of O(n), where n is the length of the input array, and it uses only constant extra space because it only uses a single variable (result) to store the XOR result.
