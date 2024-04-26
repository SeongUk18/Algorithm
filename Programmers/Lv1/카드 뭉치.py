from collections import deque

def solution(cards1, cards2, goal):
    card1 = deque(cards1)
    card2 = deque(cards2)
    goal = deque(goal)
    c1 = card1.popleft()
    c2 = card2.popleft()
    g = goal.popleft()
    while goal:
        if g == c1:
            g = goal.popleft()
            if card1:
                c1 = card1.popleft()
        elif g == c2:
            g = goal.popleft()
            if card2:
                c2 = card2.popleft()
        else:
            return 'No'
    if g == c1 or g == c2:
        return 'Yes'
    else:
        return "No"