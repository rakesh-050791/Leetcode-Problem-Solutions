# 73. Set Matrix Zeroes

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

 

# Example 1:

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Example 2:

# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


# Approach 1 : # Brute Force approach : using extra space 

class Solution:
    def setZeroes(self, matrix):
    	r = len(matrix)
    	c = len(matrix[0])

    	rows = set()
    	cols = set()

    	for i in range(r):
    		for j in range(c):
    			if matrix[i][j] == 0:
    				rows.add(i)
    				cols.add(j)

    	for i in range(r):
    		for j in range(c):
    			if i in rows or j in cols:
    				matrix[i][j] = 0


# TC : O(M*N)
# SC : O(M + N)

# Approach 2 : Optimised Approach, without extra space.

# Hints 

# Most optimized using O(1) space: But, we can do even better, O(1) - initial ask of the problem. What if instead of having a separate array to track the zeroes, we simply use the first row or col to track them and then go back to update the first row and col with zeroes after we're done replacing it? The approach to get constant space is to use first row and first col of the matrix as a tracker.

# At each row or col, if you see a zero, then mark the first row or first col as zero with the current row and col.
# Then iterate through the array again to see where the first row and col were marked as zero and then set that row/col as 0.
# After doing that, you'll need to traverse through the first row and/or first col if there were any zeroes there to begin with and set everything to be equal to 0 in the first row and/or first col.
# Time complexity for all three progression is O(m * n).

# Space: O(1) for modification in place and using the first row and first col to keep track of zeros instead of zeroes_row and zeroes_col


class Solution:
    def setZeroes(self, matrix):
    	r = len(matrix)
    	c = len(matrix[0])

    	first_row_has_zero = False
    	first_col_has_zero = False


    	# iterate through matrix to mark the zero row and cols

    	for row in range(r):
    		for col in range(c):
    			if matrix[row][col] == 0:
    				if row == 0:
    					first_row_has_zero = True
    				if col == 0:
    					first_col_has_zero = True

    				matrix[row][0] = 0 
    				matrix[0][col] = 0

    	#iterate through matrix to update the cell to be zero if it's in a zero row or col

    	for row in range(1, r):
    		for col in range(1, c):
    			if matrix[row][0] == 0 or matrix[0][col] == 0:
    				matrix[row][col] = 0
    			else:
    				matrix[row][col]

    	
    	# update the first row and col if they're zero

    	if first_row_has_zero:
    		for col in range(c):
    			matrix[0][col] = 0

    	if first_col_has_zero:
    		for row in range(r):
    			matrix[row][0] = 0

# TC : O(M*N)
# SC : O(1)


# To Run the program

matrix = [[1,1,1],[1,0,1],[1,1,1]]
sol = Solution()
response = sol.setZeroes(matrix)
print(response)


# Code Visualiser

# https://pythontutor.com/render.html#code=class%20Solution%3A%0A%20%20%20%20def%20setZeroes%28self,%20matrix%29%3A%0A%20%20%20%20%20%20%20%20r%20%3D%20len%28matrix%29%0A%20%20%20%20%20%20%20%20c%20%3D%20len%28matrix%5B0%5D%29%0A%0A%20%20%20%20%20%20%20%20first_row_has_zero%20%3D%20False%0A%20%20%20%20%20%20%20%20first_col_has_zero%20%3D%20False%0A%0A%0A%20%20%20%20%20%20%20%20%23%20iterate%20through%20matrix%20to%20mark%20the%20zero%20row%20and%20cols%0A%0A%20%20%20%20%20%20%20%20for%20row%20in%20range%28r%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20for%20col%20in%20range%28c%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20matrix%5Brow%5D%5Bcol%5D%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20row%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20first_row_has_zero%20%3D%20True%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20col%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20first_col_has_zero%20%3D%20True%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20matrix%5Brow%5D%5B0%5D%20%3D%200%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20matrix%5B0%5D%5Bcol%5D%20%3D%200%0A%0A%20%20%20%20%20%20%20%20%23iterate%20through%20matrix%20to%20update%20the%20cell%20to%20be%20zero%20if%20it's%20in%20a%20zero%20row%20or%20col%0A%0A%20%20%20%20%20%20%20%20for%20row%20in%20range%281,%20r%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20for%20col%20in%20range%281,%20c%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20matrix%5Brow%5D%5B0%5D%20%3D%3D%200%20or%20matrix%5B0%5D%5Bcol%5D%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20matrix%5Brow%5D%5Bcol%5D%20%3D%200%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20matrix%5Brow%5D%5Bcol%5D%0A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%23%20update%20the%20first%20row%20and%20col%20if%20they're%20zero%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20if%20first_row_has_zero%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20for%20col%20in%20range%28c%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20matrix%5B0%5D%5Bcol%5D%20%3D%200%0A%0A%20%20%20%20%20%20%20%20if%20first_col_has_zero%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20for%20row%20in%20range%28r%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20matrix%5Brow%5D%5B0%5D%20%3D%200%0A%20%20%20%20%20%20%20%20%0Amatrix%20%3D%20%5B%5B1,1,1%5D,%5B1,0,1%5D,%5B1,1,1%5D%5D%0Asol%20%3D%20Solution%28%29%0Aresponse%20%3D%20sol.setZeroes%28matrix%29%0Aprint%28response%29&cumulative=false&curInstr=59&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false



        