def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half

    return -1  # Target not found

# Example sorted array
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Target value to search for
target = 7

# Using the iterative approach
index_iterative = binary_search_iterative(arr, target)
print(f"Iterative: Target found at index {index_iterative}")
