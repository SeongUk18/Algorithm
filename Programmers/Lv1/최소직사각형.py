def solution(sizes):
    height = []
    width = []
    for size in sizes:
        height.append(max(size))
        width.append(min(size))
    return max(height) * max(width)