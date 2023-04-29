# 102. Binary Tree Level Order Traversal #BFS #Tree #Level-order-tracersal #using-deque


# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        myQueue = deque()
        myQueue.append(root)
        output = []
        
        while myQueue:
            level = []
            queueSize = len(myQueue)

            for _ in range(queueSize):
                node = myQueue.popleft()
                if node:
                    level.append(node.val)
                    myQueue.append(node.left)
                    myQueue.append(node.right)

            if level:
                output.append(level)
        
        return output


# Driver code to test the actual code 

# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

# obj = Solution()
# response = obj.levelOrder(root)
# print("response =", response)


# Complexity :
# Time complexity : O(n), will iterate through / visit every node atleast once
# Space complexity : O(n), using deque

# Video reference 
# https://www.youtube.com/watch?v=6ZnyEApgFYg

