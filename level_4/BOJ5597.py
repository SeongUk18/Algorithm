student_list = [_ for _ in range(1, 31)]

for i in range(28):
    student_list.remove(int(input()))

print(student_list[0])
print(student_list[1])