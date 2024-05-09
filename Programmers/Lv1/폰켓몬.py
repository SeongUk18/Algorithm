def solution(nums):
    answer = 0
    num_set = set(nums)
    if len(nums) / 2 > len(num_set):
        answer = len(num_set)
    else:
        answer = len(nums) / 2
    return answer