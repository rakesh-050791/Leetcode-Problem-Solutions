# 142. Linked List Cycle II ||  #Linked-List #Slow-fast-pointer-apprach #two-pointers

# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

# Do not modify the linked list.

 

# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.
# Example 2:


# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.
# Example 3:


# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.





# Solution Approach 

# Intuition :
# Use a Floyd's Cycle-Finding algorithm to detect a cycle in a linked list and find the node where the cycle starts.
# What is Floyd's Cycle-Finding algorithm ?
# It is also called Hare-Tortoise algorithm
# The algorithm works by using two pointers, a slow pointer and a fast pointer.
# Initially, both pointers are set to the head of the linked list.
# The fast pointer moves twice as fast as the slow pointer.
# If there is a cycle in the linked list, eventually, the fast pointer will catch up with the slow pointer.
# If there is no cycle, the fast pointer will reach the end of the linked list.
# Approach :
# When the two pointers meet, we know that there is a cycle in the linked list.
# We then reset the slow pointer to the head of the linked list and move both pointers at the same pace, one step at a time, until they meet again.
# The node where they meet is the starting point of the cycle.
# If there is no cycle in the linked list, the algorithm will return null.
# Let's understand this with an Example :
# Let's say we have a linked list with a cycle, like the one below:
# 1 -> 2 -> 3 -> 4 -> 5 -> 2
# To detect the cycle and find the starting point, we use two pointers, a slow pointer and a fast pointer, initially set to the head of the linked list.
# slow = 1
# fast = 1
# Then we move the pointers through the linked list. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time.
# slow = 2
# fast = 3

# slow = 3
# fast = 5

# slow = 4
# fast = 2
# Eventually, the fast pointer will catch up with the slow pointer, which means that there is a cycle in the linked list.
# slow = 5
# fast = 4
# At this point, we reset the slow pointer to the head of the linked list, and move both pointers one step at a time until they meet again.
# slow = 1
# fast = 4

# slow = 2
# fast = 5

# slow = 3
# fast = 2
# The node where they meet is the starting point of the cycle, which in this case is node 2.
# So, the algorithm returns node 2 as the starting point of the cycle.
# I hope this visual explanation helps you understand the Floyd's Cycle-Finding algorithm better.

class Solution:
    def detectCycle(self, head: ListNode) -> Optional[ListNode]:
        slow, fast = head, head
        isCyclePresent = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                isCyclePresent = True
                break

        point1 = head 
        point2 = fast

        if isCyclePresent:
            while(point1 != point2):
                point1 = point1.next
                point2 = point2.next

            return point1
        else:
            return None


# Complexity :
# Time complexity : O(n)
# Space complexity : O(1)