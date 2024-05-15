def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array is:", arr)


### Explanation

#### Selection Sort:
    # 1. Iterate over the entire array.
    # 2. For each position in the array, find the smallest element in the unsorted portion of the array.
    # 3. Swap the found minimum element with the first unsorted position.
    # 4. Repeat until the entire array is sorted.

