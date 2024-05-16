def solution(genres, plays):
    answer = []
    gen_dic = {}
    count_dic = {}
    for i in range(len(genres)):
        if genres[i] in gen_dic:
            gen_dic[genres[i]] += plays[i]
            count_dic[genres[i]].append((plays[i], i))
        else:
            gen_dic[genres[i]] = plays[i]
            count_dic[genres[i]] = [(plays[i], i)]
    print(gen_dic)
    print(count_dic)
    gen = sorted(gen_dic.items(), key=lambda x: x[1], reverse=True)
    print(gen)

    for g, i in gen:
        print(g, i)
        sorted_song = sorted(count_dic[g], key=lambda x: (-x[0], x[1]))[:2]
        print(sorted_song)
        for song in sorted_song:
            answer.append(song[1])

    return answer