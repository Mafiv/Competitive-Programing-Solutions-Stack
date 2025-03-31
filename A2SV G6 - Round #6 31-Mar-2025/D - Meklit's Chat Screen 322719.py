# Problem: D - Meklit's Chat Screen - https://codeforces.com/gym/594077/problem/D

from collections import deque
def solve():
    n, k = map(int, input().split())
    messages = list(map(int, input().split()))
    screen = deque()
    seen = set()

    for id_i in messages:
        if id_i not in seen:
            if len(screen) == k:
                removed = screen.pop()
                seen.remove(removed)
            
            screen.appendleft(id_i)
            seen.add(id_i)

    print(len(screen))
    return screen

if __name__=="__main__":
    print(*(solve()))