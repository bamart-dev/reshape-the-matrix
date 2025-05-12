# Ada C23 - PSE 06: Merging Sorted Lists
### Problem Statement
In MATLAB, a programming platform for numeric computing, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the number of rows and number of columns of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

#### Example
Input:
nums = [[1,2],[3,4]]
r = 2, c = 4

Output:
[[1,2], [3,4]]

#### Example 2
Input:
nums = [[1,2], [3,4], [5,6], [7,8]]
r = 2, c = 4

Output:
[[1,2,3,4], [5,6,7,8]]
