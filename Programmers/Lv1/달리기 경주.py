def solution(players, callings):
    answer = []
    num_dict = {}

    for i in range(len(players)):
        num_dict[players[i]] = i

    for calling in callings:
        # 호출된 플레이어의 인덱스 가져오기
        current_idx = num_dict[calling]

        if current_idx > 0:
            # 앞에 있는 플레이어와 자리 교환
            prev_player = players[current_idx - 1]
            players[current_idx - 1], players[current_idx] = players[current_idx], players[current_idx - 1]

            # 딕셔너리 업데이트: 교환된 플레이어들의 위치 갱신
            num_dict[calling] = current_idx - 1
            num_dict[prev_player] = current_idx

    return players
