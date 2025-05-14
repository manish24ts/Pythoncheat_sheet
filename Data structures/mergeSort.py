def merge_sort(arr):
    # Base case: list with 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Divide the list into halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Step 2: Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    # Step 3: Compare elements from left and right and merge them
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Step 4: Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# -------------------------------
# 💡 Example Usage
# -------------------------------

arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted Array:", sorted_arr)
