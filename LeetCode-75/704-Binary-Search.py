# 704. Binary Search | #Binary-search #two-pointer-approach #O (log₂n)

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low <= high:

        	# in python below line will always work, but it might give integer overflow error in java, c++ etc.
            mid = (low + high) // 2

            # using below won't give overflow error in java, c++
            mid = low + ((high - low) // 2) 

            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        return -1


# Complexity :
# Time complexity : O(log₂n), will iterate through / visit every node atleast once
# Space complexity : O(n), using deque


# Video reference 
# https://www.youtube.com/watch?v=s4DPM8ct1pI

