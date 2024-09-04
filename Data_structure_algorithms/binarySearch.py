def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = [2, 3, 4, 10, 40]
target = 10
result = binary_search(arr, target)
print(f"Element found at index: {result}")  # Output: Element found at index: 3
