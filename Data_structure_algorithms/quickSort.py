def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr if pivot > x]
    middle = [x for x in arr if pivot == x]
    right = [x for x in arr if pivot < x]
    return quick_sort(left) + middle + quick_sort(right)


arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print("Sorted array is:", sorted_arr)
