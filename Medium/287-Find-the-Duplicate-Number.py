# 287. Find the Duplicate Number

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:




# Approach  1 : Modifying existing array : #Self-Tought

class Solution:
    def findDuplicate(self, nums):
    	nums.sort()
    	n = len(nums)

    	for i in range(1, n-1):
    		if (nums[i] != nums[i-1]) and (nums[i] != nums[i+1]):

    			continue
    		else:
    			return nums[i]



 # Approach 2 : Slow & Fast Pointer or Tortoise & Hare approach 

class Solution:
    def findDuplicate(self, nums):
    	tortoise = hare = nums[0]


    	# Finding the first intersection point of the two runners.
    	while True:

    		tortoise = nums[tortoise]
    		hare = nums[nums[hare]]

    		if tortoise == hare:
    			break

    	# Find the "entrance" to the cycle.

    	tortoise = nums[0]
    	while tortoise !=hare:
    		tortoise = nums[tortoise]
    		hare = nums[hare]

    	return hare
