# 54. Spiral Matrix

# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]


# Example 2:

# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100



# Approach 1 :

# matrix = [ 
# 			[1,2,3] 
# 			[4,5,6]
# 			[7,8,9]
# 		 ]

# Output = [1,2, 3,6,9, 8,7, 4,5]


class Solution:
    def spiralOrder(self, matrix):
        rows = len(matrix)
        columns = len(matrix[0])

        result = []

        #setting the initial 4 boundries
        up = left = 0
        right = columns - 1
        down = rows - 1

        while len(result) < rows * columns:

        	#Traverse from left to right
        	for col in range(left, right+1):
        		result.append(matrix[up][col])


        	#Traverse from up to down
        	for row in range(up+1, down+1):
        		result.append(matrix[row][right])


        	#Traverse from right to left
        	if up != down:
        		for col in range(right - 1 , left - 1 , -1):
        			result.append(matrix[down][col])


        	#Traverse from down to up
        	if left != right:
        		for row in range(down-1, up, -1):
        			result.append(matrix[row][left])


        	left += 1
            right -= 1
            up += 1
            down -= 1

        return result 

# Hints : Algorithm

# Initialize the top, right, bottom, and left boundaries as up, right, down, and left.
# Initialize the output array result.
# Traverse the elements in spiral order and add each element to result:
# Traverse from left boundary to right boundary.
# Traverse from up boundary to down boundary.
# Before we traverse from right to left, we need to make sure that we are not on a row that has already been traversed. If we are not, then we can traverse from right to left.
# Similarly, before we traverse from top to bottom, we need to make sure that we are not on a column that has already been traversed. Then we can traverse from down to up.
# Remember to move the boundaries by updating left, right, up, and down accordingly.
# Return result.


# Code Visualiser :

# https://pythontutor.com/render.html#code=class%20Solution%3A%0A%20%20%20%20def%20spiralOrder%28self,%20matrix%29%3A%0A%20%20%20%20%20%20%20%20rows%20%3D%20len%28matrix%29%0A%20%20%20%20%20%20%20%20columns%20%3D%20len%28matrix%5B0%5D%29%0A%0A%20%20%20%20%20%20%20%20result%20%3D%20%5B%5D%0A%0A%20%20%20%20%20%20%20%20%23setting%20the%20initial%204%20boundries%0A%20%20%20%20%20%20%20%20up%20%3D%20left%20%3D%200%0A%20%20%20%20%20%20%20%20right%20%3D%20columns%20-%201%0A%20%20%20%20%20%20%20%20down%20%3D%20rows%20-%201%0A%0A%20%20%20%20%20%20%20%20while%20len%28result%29%20%3C%20rows%20*%20columns%3A%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23Traverse%20from%20left%20to%20right%0A%20%20%20%20%20%20%20%20%20%20%20%20for%20col%20in%20range%28left,%20right%2B1%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20result.append%28matrix%5Bup%5D%5Bcol%5D%29%0A%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23Traverse%20from%20up%20to%20down%0A%20%20%20%20%20%20%20%20%20%20%20%20for%20row%20in%20range%28up%2B1,%20down%2B1%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20result.append%28matrix%5Brow%5D%5Bright%5D%29%0A%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23Traverse%20from%20right%20to%20left%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20up%20!%3D%20down%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20for%20col%20in%20range%28right%20-%201%20,%20left%20-%201%20,%20-1%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20result.append%28matrix%5Bdown%5D%5Bcol%5D%29%0A%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23Traverse%20from%20down%20to%20up%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20left%20!%3D%20right%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20for%20row%20in%20range%28down-1,%20up,%20-1%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20result.append%28matrix%5Brow%5D%5Bleft%5D%29%0A%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20left%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20right%20-%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20up%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20down%20-%3D%201%0A%0A%20%20%20%20%20%20%20%20return%20result%20%0A%20%20%20%0A%20%20%20%20%20%20%20%20%0Amatrix%20%3D%20%5B%5B1,2,3%5D,%5B4,5,6%5D,%5B7,8,9%5D%5D%0Asol%20%3D%20Solution%28%29%0Aresponse%20%3D%20sol.spiralOrder%28matrix%29%0Aprint%28response%29&cumulative=false&curInstr=51&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false


