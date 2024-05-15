def solution(arr):
    answer = []
    pre = arr[0]
    answer.append(pre)
    for i in arr[1:]:
        if pre == i:
            continue
        else:
            answer.append(i)
            pre = i

    return answer