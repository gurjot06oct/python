## Problem Statement: Fibonacci Series with List Comprehension

### Objective:

Write a Python program that generates the Fibonacci series up to the n-th element using list comprehension. The program should take an integer input `n` and output a list containing the first `n+1` elements of the Fibonacci series.

### Requirements:

1. The program should prompt the user to enter an integer `n`.
2. Using list comprehension, the program should generate the first `n+1` elements of the Fibonacci series.
3. The Fibonacci series is defined as:
   - F(0) = 0
   - F(1) = 1
   - F(n) = F(n-1) + F(n-2) for n >= 2
4. The program should not use recursion to generate the series.

### Input:

- An integer `n` (where ( n > 0 )).

### Output:

- A list containing the first `n+1` elements of the Fibonacci series.

### Example:

    For `n = 10`, the output should be:
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

### Implementation Details:

- You can use a loop inside the list comprehension to compute the Fibonacci series iteratively.
- Make sure to handle the cases where `n` is 0 or 1 appropriately.
