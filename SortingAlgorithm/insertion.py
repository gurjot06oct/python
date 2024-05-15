def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage
arr = [64, 25, 12, 22, 11]
insertion_sort(arr)
print("Sorted array is:", arr)


### Explanation

#### Insertion Sort:
    # 1. Iterate from the second element to the end of the array.
    # 2. For each element, compare it with elements in the sorted portion (to its left).
    # 3. Shift elements in the sorted portion to the right to make room for the current element.
    # 4. Insert the current element into its correct position.
    # 5. Repeat until the entire array is sorted.