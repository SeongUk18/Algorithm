string = input()

# 해당되는 값이면 1문자이기 때문에 임의의 문자로 변환시킴
if 'c=' in string:
    string = string.replace('c=', 'A')
if 'c-' in string:
    string = string.replace('c-', 'A')
if 'dz=' in string:
    string = string.replace('dz=', 'A')
if 'd-' in string:
    string = string.replace('d-', 'A')
if 'lj' in string:
    string = string.replace('lj', 'A')
if 'nj' in string:
    string = string.replace('nj', 'A')
if 's=' in string:
    string = string.replace('s=', 'A')
if 'z=' in string:
    string = string.replace('z=', 'A')

print(len(string))
