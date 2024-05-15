def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1  # Target not found

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid  # Target found
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)  # Search in the right half
    else:
        return binary_search_recursive(arr, target, left, mid - 1)  # Search in the left half

# Example sorted array
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Target value to search for
target = 7

# Using the recursive approach
index_recursive = binary_search_recursive(arr, target, 0, len(arr) - 1)
print(f"Recursive: Target found at index {index_recursive}")
