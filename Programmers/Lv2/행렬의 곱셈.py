def solution(arr1, arr2):
    m1, n1 = len(arr1), len(arr1[0])
    m2, n2 = len(arr2), len(arr2[0])
    num = 0
    test = []
    answer = []
    # print(m1, n1, m2, n2)
    for j in range(m1):
        for i in range(n2):
            for k in range(n1):
                num += arr1[j][k] * arr2[k][i]
            print(num)
            test.append(num)
            num = 0
        print(test)
        answer.append(test)
        test = []
    print(answer)
    return answer