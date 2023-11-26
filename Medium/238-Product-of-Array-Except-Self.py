# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)


# class Solution:
#     def productExceptSelf(self, nums):
#     	n = len(nums)
#     	prefixProduct = []
#     	prefixProduct.append(0)
#     	suffixProduct = []

#     	for i in range(1, n+1):
#     		prefixProduct[i] *= prefixProduct[i-1]

#     	return prefixProduct



# Approach 1 :

class Solution:
    def productExceptSelf(self, nums):
    	n = len(nums)
    	prefixProduct , suffixProduct, result = [0] * n, [0] * n, [0] * n

    	prefixProduct[0] = 1

    	for i in range(1, n):
    		prefixProduct[i] = prefixProduct[i-1] * nums[i-1]


    	suffixProduct[n-1] = 1

    	for j in range(n-2, -1, -1):
    		suffixProduct[j] = suffixProduct[j+1] * nums[j+1]


    	for k in range(n):
    		result[k] = prefixProduct[k] * suffixProduct[k]

    	return result


# Hints 

# Here are some hints:

# Initialize two arrays: Create two arrays, say prefix and suffix, of the same length as the input array nums.

# Calculate prefix products: Iterate through the array from left to right and fill in the prefix array. For each element nums[i], prefix[i] should store the product of all elements to the left of nums[i].

# Calculate suffix products: Iterate through the array from right to left and fill in the suffix array. For each element nums[i], suffix[i] should store the product of all elements to the right of nums[i].

# Compute the final result: For each element nums[i], the result answer[i] is the product of prefix[i] and suffix[i].


