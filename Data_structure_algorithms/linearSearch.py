def linear_search(arr, target):
    for idx, num in enumerate(arr):
        if num == target:
            return idx


arr = [3, 5, 2, 4, 9]
target = 4
result = linear_search(arr, target)
print(f"Element found at index: {result}")  # Output: Element found at index: 3
