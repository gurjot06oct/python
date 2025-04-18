**Problem Statement: 2D Array Rotation**

You are given a square 2D array (matrix) of dimensions `k x k`, initialized with consecutive numbers from 1 to `k*k` arranged row-wise. Your task is to rotate this matrix clockwise or anticlockwise based on a given rotation index.

Write a program that performs the following steps:

1. Prompt the user to input the dimensions (`k`) of the square matrix.
2. Initialize the 2D array `array2d` with dimensions `k x k`, where each element is takes as input.
3. Accept an integer input `n` representing the rotation index. If `n` is positive, rotate the matrix clockwise; if negative, rotate it anticlockwise; if `n` is zero, print the original matrix and exit.
4. Rotate the matrix according to the rotation index and print the rotated matrix.

Your program should handle the rotation of the matrix efficiently using the following steps:

- Determine the direction of rotation (`clockwise`(+) or `anticlockwise` (-)) based on the sign of the rotation index.

**Constraints:**

- You must implement the solution without using external libraries such as NumPy, Python arrays, or any other array-specific libraries.
- Your solution must not exceed the use of 4 loops in total. This includes loops used for iteration, such as `for` or `while` loops, and excludes any nested loops inside comprehensions.

**Example:**

```
Dimensions: 3
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
Rotation Index: -1

Output:
[2, 3, 6]
[1, 5, 9]
[4, 7, 8]
```
