# 448. Find All Numbers Disappeared in an Array

# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the 
# range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]


# Approach 1 : Brute force : Self thought : Wrong answer
# nums = [4,3,2,7,8,2,3,1]

# SortedNums = [1,2,2,3,3,4,7,8]

class Solution:
    def findDisappearedNumbers(self, nums):
    	nums.sort()
    	lastNum = nums[-1]
    	tempList = []

    	for indx in range(lastNum-1):
    		if (nums[indx] != nums[indx + 1] and nums[indx] == nums[indx + 1] - 1) or  nums[indx] == nums[indx + 1]:
    			continue
    		else:
    			tempList.append(nums[indx] + 1)

    	return tempList


# Approach 2 : 

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            newIndex = abs(num) - 1

            if nums[newIndex] > 0:
                nums[newIndex] *= -1


        result = []

        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                result.append(i)

        return result


## Hints

# Since we are given this information, we can make use of the input array itself to somehow mark visited numbers and then find our missing numbers. Now, we don't want to change the actual data in the array but who's stopping us from changing the magnitude of numbers in the array? That is the basic idea behind this algorithm.

# We will be negating the numbers seen in the array and use the sign of each of the numbers for finding our missing numbers. We will be treating numbers in the array as indices and mark corresponding locations in the array as negative.

# Algorithm

# Iterate over the input array one element at a time.
# For each element nums[i], mark the element at the corresponding location negative if it's not already marked so i.e. nums[  nums[i]  −1  ]×−1nums[\; nums[i] \;- 1\;] \times -1nums[nums[i]−1]×−1 .
# Now, loop over numbers from 1⋯N1 \cdots N1⋯N and for each number check if nums[j] is negative. If it is negative, that means we've seen this number somewhere in the array.
# Add all the numbers to the resultant array which don't have their corresponding locations marked as negative in the original array.
