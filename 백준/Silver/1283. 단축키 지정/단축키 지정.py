N = int(input())

short = set()

for _ in range(N):
    word = input()

    word_list = word.split()

    found = False

    for i, w in enumerate(word_list):
        if w[0].upper() not in short:
            short.add(w[0].upper())
            word_list[i] =  "[" + w[0] + "]" + w[1:]
            found = True
            word = " ".join(word_list)
            break

    if not found:
        for i, c in enumerate(word):
            if c == " ":
                continue

            if c.upper() not in short:
                short.add(c.upper())
                word = word[:i] + "[" + word[i] + "]" + word[i + 1:]
                found = True
                break

    print(word)
