# 98. Validate Binary Search Tree | #Binary-Search-Tree #BST #DFS

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left 
# subtree
#  of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [2,1,3]
# Output: true
# Example 2:


# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float("-inf"), float("inf"))

    def dfs(self, root, leftLimit, rightLimit):
        if not root:
            return True 

        if not (root.val < rightLimit and root.val > leftLimit):
            return False 
        
        return ( self.dfs(root.left, leftLimit, root.val) and 
        self.dfs(root.right, root.val, rightLimit))


# OR


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(float("-inf"), float("inf"), root)

    def dfs(self, leftLimit, rightLimit, root):
        if not root:
            return True 
        elif (root.val <= leftLimit or  root.val >= rightLimit):
            return False 
        else:
            return ( self.dfs(leftLimit, root.val, root.left) and 
                    
                    self.dfs(root.val, rightLimit, root.right))



# video reference :
# https://www.youtube.com/watch?v=s6ATEkipzow
# https://www.youtube.com/watch?v=iU0n2SoRA8M