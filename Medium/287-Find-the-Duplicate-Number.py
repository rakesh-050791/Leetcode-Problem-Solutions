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



# Dry-run

# Let us do a dry run to understand better the approach behind the code :
# nums = [1,3,4,2,2]
# slow = nums[0] = 1
# fast = nums[0] = 1
# slow = nums[1] = 3
# fast = nums[nums[1]] = nums[3] = 2
# since these two are not equal we update the values ,
# slow = nums[3] = 2
# fast = nums[nums[2]] = nums[4] = 2
# Now since these are equal , we exit the loop.
# Now fast = nums[0] = 1
# slow!=fast , 
# slow = nums[2] = 4
# fast = nums[1] = 3
# slow!=fast so ,
# slow = nums[4] = 2
# fast = nums[3] = 2
# Now slow and fast are equal so , the repeating element is 2.
# Intution : The basic thinking is that we keep two counter variables, slow is incremented by +1 and fast by +2 and 
# at one point they will be pointing to the repeating elements, which is returned by the slow pointer. 


# Links for different approaches

## https://medium.com/nerd-for-tech/find-the-duplicate-number-aaf426ded83d 

## https://takeuforward.org/data-structure/find-the-duplicate-in-an-array-of-n1-integers/