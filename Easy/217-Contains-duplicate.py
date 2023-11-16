# 217 - Contains Duplicate


# Question :

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true


# My Initial Approach



# Approach 1 :  Wrong answer

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        totalNums = len(nums)

        if totalNums == 1:
            return True

        nums = nums.sort()
        for i in range(totalNums-1):
            if nums[i+1] == nums[i]:
                return True
            else:
                i+=1
        return False




# Approach 2 : Using sort

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        totalNums = len(nums)

        if totalNums == 1:
            return False

        nums.sort()
        for i in range(totalNums-1):
            if nums[i] == nums[i+1]:
                return True
            i+=1
        return False

TC : O(nlogn)
SC : 0(1)


# Approach 3 : Using Hashmap

# 3.1 -> Working
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        totalNums = len(nums)

        if totalNums == 1:
            return False

        mySet = set()

        for num in nums:
            if num in mySet:
                return True
            mySet.add(num)
        return False

TC : O(n)
SC : 0(n)
