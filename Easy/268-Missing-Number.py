# 268. Missing Number

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
# Example 2:

# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
# Example 3:

# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 

# Constraints:

# n == nums.length
# 1 <= n <= 104
# 0 <= nums[i] <= n
# All the numbers of nums are unique.
 

# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?



# Hints 

# Properties of XOR 

# X -> Any Element 

# X ^ X = 0
# 0 ^ X = X 
# X ^ Y = Y ^ X

# XOR is commutative and associative, meaning the order of XOR operations doesn't matter.

# The idea is to XOR all the numbers from 0 to n and then XOR the result with all the numbers in the given array. The remaining value after these XOR operations will be the missing number.

# Here's a step-by-step explanation:

# XOR all numbers from 0 to n: This can be done by XORing the numbers in the array nums along with the index.

# XOR all numbers in the array nums.

# The result of step 1 XORed with the result of step 2 will give the missing number.


# Approach 1 : Using XOR 
class Solution:
    def missingNumber(self, nums):

    	expectedXOR = 0
    	for i in range(len(nums) + 1):
    		expectedXOR ^= i

    	actualXOR = 0
    	for num in nums:
    		actualXOR ^= num

    	return expectedXOR ^ actualXOR

TC : O(n)
SC : O(1)

# Note** : This problem can be done using Sort() or using hashset, but that won't be the optimal solution.

# Visualise here : https://pythontutor.com/visualize.html#code=class%20Solution%3A%0A%20%20%20%20def%20missingNumber%28self,%20nums%29%3A%0A%0A%20%20%20%20%20%20%20%20expectedXOR%20%3D%200%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%28len%28nums%29%20%2B%201%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22----%20i%20----%20%3D%20%22,%20i%29%0A%20%20%20%20%20%20%20%20%20%20%20%20expectedXOR%20%5E%3D%20i%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22****%20expectedXOR%20****%20%3D%20%22,%20expectedXOR%29%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28'%5Cn'%29%0A%0A%20%20%20%20%20%20%20%20print%28%22%24%24%24%24%20expectedXOR%20%24%24%24%24%20%3D%20%22,%20expectedXOR%29%0A%20%20%20%20%20%20%20%20print%28'%5Cn'%29%0A%0A%20%20%20%20%20%20%20%20actualXOR%20%3D%200%0A%20%20%20%20%20%20%20%20for%20num%20in%20nums%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22****%20num%20****%20%3D%20%22,%20num%29%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20actualXOR%20%5E%3D%20num%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22****%20actualXOR%20****%20%3D%20%22,%20actualXOR%29%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28'%5Cn'%29%0A%0A%20%20%20%20%20%20%20%20print%28%22!!!!%20actualXOR%20!!!!%20%3D%20%22,%20actualXOR%29%0A%20%20%20%20%20%20%20%20print%28'%5Cn'%29%0A%0A%20%20%20%20%20%20%20%20return%20expectedXOR%20%5E%20actualXOR%0A%0A%0Anums%20%3D%20%5B3,0,1%5D%0Asol%20%3D%20Solution%28%29%0Aresponse%20%3D%20sol.missingNumber%28nums%29%0Aprint%28response%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false


# nums = [3,0,1]
# sol = Solution()
# response = sol.missingNumber(nums)
# print(response)


