start = input()

end = input()
flag = False

def change(word):
    global start
    global flag
    # print(word)
    if flag:
        return

    if start == word:
        flag = True
        return 
    
    if len(word) <= len(start):
        return

    if word[-1] == "A":
        change(word[:-1])
    if word[0] == "B":
        change(word[1:][::-1])
    
    

change(end)

if flag:
    print(1)
else:
    print(0)