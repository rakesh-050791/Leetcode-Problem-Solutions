# 283. Move Zeroes

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
 

# Follow up: Could you minimize the total number of operations done?

class Solution:
    def moveZeroes(self, nums):
    	placeForNonZeroElement = 0

    	for i in range(len(nums)):
    		if nums[i] != 0:
    			nums[i], nums[placeForNonZeroElement] = nums[placeForNonZeroElement], nums[i]

    			placeForNonZeroElement += 1


# Hints : 

# This solution uses a two-pointer approach. The placeForNonZeroElement pointer keeps track of the position where the next non-zero element should be placed. As you iterate through the array, whenever you encounter a non-zero element, you swap it with the element at the placeForNonZeroElement and then increment the placeForNonZeroElement. This way, all non-zero elements are moved to the front of the array, and zeros are pushed to the end.

# This solution has a time complexity of O(n), where n is the length of the array, as it makes a single pass through the array. It also minimizes the total number of operations done, as it only performs swaps when necessary




