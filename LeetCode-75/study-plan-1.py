								# https://leetcode.com/study-plan/leetcode-75


# 1 : 1480. Running Sum of 1d Array | #array #prefix-sum #running-sum


# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Example 2:

# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
# Example 3:

# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pf = [0] * n
        pf[0] = nums[0]

        for i in range(1, n):
            pf[i] = pf[i-1] + nums[i]
            
        return pf


# Complexity Analysis

# Time complexity: O(n) where n is the length of the input array. This is because we use a single loop that iterates over the entire array to calculate the running sum.

# Space complexity: O(1) since we don't use any additional space to find the running sum. Note that we do not take into consideration the space occupied by the output array.



# 2 : 724. Find Pivot Index | #aray #sum-of-array-elements

# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.

 

# Example 1:

# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11
# Example 2:

# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.
# Example 3:

# Input: nums = [2,1,-1]
# Output: 0
# Explanation:
# The pivot index is 0.
# Left sum = 0 (no elements to the left of index 0)
# Right sum = nums[1] + nums[2] = 1 + -1 = 0


# Solution Approach : 

# We need to quickly compute the sum of values to the left and the right of every index.

# Let's say we knew totalSum as the sum of the numbers, and we are at index i. If we knew the sum of numbers leftsum that are to the left of index i, then the other sum to the right of the index would just be totalSum - nums[i] - leftsum.

# As such, we only need to know about leftsum to check whether an index is a pivot index in constant time. Let's do that: as we iterate through candidate indexes i, we will maintain the correct value of leftsum.


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        totalSum = sum(nums)
        leftSum = 0

        for indx, val in enumerate(nums):
            if leftSum == (totalSum - nums[indx] - leftSum):
                return indx
            leftSum += val
        
        return -1


# Complexity Analysis

# Time Complexity: O(N), where N is the length of nums.

# Space Complexity: O(1), the space used by leftsum and totalSum.



# 3 : 205. Isomorphic Strings | #hashing #Strings #Sub-strings

# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# Output: false
# Example 3:

# Input: s = "paper", t = "title"
# Output: true

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mapST, mapTS = {}, {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            
            if ((c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1)):
                return False
            mapST[c1] = c2
            mapTS[c2] = c1

        return True


# Complexity Analysis

# Time Complexity: O(N), where N is the length of strings (linear time).

# Space Complexity: O(N), used hashmap to store chars frequency.


# 4 : 392. Is Subsequence #Strings #Two-pointer

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 

# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        # OR

        # while i < len(s) and j < len(t):
        #     if s[i] == t[j]:
        #         i += 1    
        #     j += 1


        return True if i == len(s) else False


# Complexity Analysis

# Time Complexity: O(N), where N is the length of strings (linear time).

# Space Complexity: O(1), no extra space used


# 5 : 21. Merge Two Sorted Lists # Linked-list

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.


# Example 1:

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:

# Input: list1 = [], list2 = []
# Output: []

# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
                tail = tail.next
            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next

        if list1:
            tail.next = list1 
        elif list2:
            tail.next = list2 

        return dummy.next


# 6 : 206. Reverse Linked List #Linked=list #two-pointers

# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Below is the iterative approach using #two-pointers
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev, curr = None, head
    
        while curr:
            temp = curr.next

            curr.next = prev
            prev = curr

            curr = temp
        
        return prev


# Complexity Analysis

# Time Complexity: O(N).

# Space Complexity: O(1), no extra space used.

# Below is the recursive approach for the same 

class Solution:
    def reverseList(self, head: ListNode) -> Optional[ListNode]:
        
        if head is None:
            return None

        newHead = head

        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        
        head.next = None

        return newHead

# Complexity Analysis

# Time Complexity: O(N).

# Space Complexity: O(N).


# 7 : 876. Middle of the Linked List #Linked-List #Slow-fast-pointer-apprach #two-pointers
 
# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# Example 2:


# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
