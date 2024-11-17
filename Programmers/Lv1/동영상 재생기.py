def min_to_sec(time):
    min_time = int(time[:2])
    sec_time = int(time[3:])

    return min_time * 60 + sec_time


def sec_to_min(seconds):
    min_time = seconds // 60
    sec_time = seconds % 60

    return f"{min_time:02}:{sec_time:02}"


def solution(video_len, pos, op_start, op_end, commands):
    video_sec = min_to_sec(video_len)
    pos_sec = min_to_sec(pos)
    op_start_sec = min_to_sec(op_start)
    op_end_sec = min_to_sec(op_end)

    for c in commands:
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec
        # print(pos_sec)
        if c == "next":
            if pos_sec + 10 <= video_sec:
                pos_sec += 10
            else:
                pos_sec = video_sec
        elif c == "prev":
            if pos_sec - 10 >= 0:
                pos_sec -= 10
            else:
                pos_sec = 0
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec

    return sec_to_min(pos_sec)
