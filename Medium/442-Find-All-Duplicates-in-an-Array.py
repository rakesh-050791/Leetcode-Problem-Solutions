# 442. Find All Duplicates in an Array

# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only constant extra space.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1,2]
# Output: [1]
# Example 3:

# Input: nums = [1]
# Output: []
 

# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
# Each element in nums appears once or twice.




class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:


# Approach 1 : 


class Solution:
    def findDuplicates(self, nums):
    	result = []
    	for num in nums:
    		nums[abs(num) - 1] *= -1

    	for num in nums:
    		if nums[abs(num) - 1] > 0:
    			result.append(abs(num))
    			nums[abs(num) - 1] *= -1

    	return result


# Approach 1.1


class Solution:
    def findDuplicates(self, nums):
        result = []
        for num in nums:
            print("BEFORE ***** num *****", num)

            print("BEFORE ***** nums[abs(num) - 1] *****", nums[abs(num) - 1])
            if nums[abs(num) - 1] < 0:
                result.append(abs(num))

            nums[abs(num) - 1] *= -1
            print('\n')
            print("AFTER ***** nums[abs(num) - 1] *****", nums[abs(num) - 1])
            print('\n')
        return result
        
nums = [4,3,2,7,8,2,3,1]
sol = Solution()
response = sol.findDuplicates(nums)
print(response)


# Hints 
### **Mark Visited Elements in the Input Array itself**

# **Intuition**

# All the above approaches have ignored a key piece of information in the problem statement:

# > The integers in the input array arr satisfy 1 ≤ arr[i] ≤ n, where n is the size of array. 2
# > 

# This presents us with two key insights:

# 1. All the integers present in the array are positive.i.e. `arr[i] > 0` for any valid index `i`.
    
#     [3](https://leetcode.com/problems/find-all-duplicates-in-an-array/editorial/#user-content-fn-note-4-1)
    
# 2. The decrement of any integers present in the array must be an accessible index in the array.i.e. for any integer `x` in the array, `x-1` is a valid index, and thus, `arr[x-1]` is a valid reference to an element in the array.
    
#     [4](https://leetcode.com/problems/find-all-duplicates-in-an-array/editorial/#user-content-fn-note-4-2)
    

# **Algorithm**

# 1. Iterate over the array and for every element `x` in the array, negate the value at index `abs(x)-1`.
    
#     [5](https://leetcode.com/problems/find-all-duplicates-in-an-array/editorial/#user-content-fn-note-4-3)
    
#     - The negation operation effectively marks the value `abs(x)` as *seen / visited*.

# > Pop Quiz: Why do we need to use abs(x), instead of x?
# > 
# 1. Iterate over the array again, for every element `x` in the array:
#     - If the value at index `abs(x)-1` is positive, it must have been negated twice. Thus `abs(x)` must have appeared twice in the array. We add `abs(x)` to the result.
#     - In the above case, when we reach the second occurrence of `abs(x)`, we need to avoid fulfilling this condition again. So, we'll additionally negate the value at index `abs(x)-1`.

# > Pop Quiz: Can you do this in a single loop?
# > 

# Definitely! Notice that if an element `x` occurs just once in the array, the value at index `abs(x)-1` becomes negative and remains so for all of the iterations that follow.

# 1. Traverse through the array. When we see an element `x` for the first time, we'll negate the value at index `abs(x)-1`.
# 2. But, the next time we see an element `x`, we *don't* need to negate again! If the value at index `abs(x)-1` is already negative, we know that we've seen element `x` before.

# So, now we are relying on a single negation to mark the visited status of an element. This is similar to what we did in [Approach 3](https://leetcode.com/problems/find-all-duplicates-in-an-array/editorial/#approach-3-store-seen-elements-in-a-set), except that we are re-using the array (with some smart negations) instead of a separate set.
