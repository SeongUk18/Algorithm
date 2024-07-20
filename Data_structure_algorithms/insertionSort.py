def insertion_sort(arr):
    for i in range(1, len(arr)):
        n = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > n:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = n


arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Sorted array is:", arr)
