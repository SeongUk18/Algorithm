from collections import Counter

n = int(input())
start_str = input()
start_counter = Counter(start_str)
answer = 0

for _ in range(n - 1):
    compare_str = input()
    compare_counter = Counter(compare_str)
    
    plus = 0
    minus = 0
    
    all_chars = set(start_counter.keys()) | set(compare_counter.keys())
    
    for char in all_chars:
        diff = start_counter.get(char, 0) - compare_counter.get(char, 0)
        if diff > 0:
            plus += diff
        else:
            minus -= diff

    if plus <= 1 and minus <= 1:
        answer += 1

print(answer)