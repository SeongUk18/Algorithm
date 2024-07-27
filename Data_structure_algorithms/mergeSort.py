def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    center = len(arr) // 2
    left = arr[:center]
    right = arr[center:]

    left_sort = merge_sort(left)
    right_sort = merge_sort(right)

    return merge(left_sort, right_sort)


def merge(left, right):
    new_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new_arr.append(left[i])
            i += 1
        else:
            new_arr.append(right[j])
            j += 1

    new_arr.extend(left[i:])
    new_arr.extend(right[j:])

    return new_arr


arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array is:", sorted_arr)
