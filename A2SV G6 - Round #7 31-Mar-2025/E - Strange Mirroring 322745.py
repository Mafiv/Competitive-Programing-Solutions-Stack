# Problem: E - Strange Mirroring - https://codeforces.com/gym/596141/problem/E

def get_character(level, position, idx, base_str):
    if level == 1: 
        return base_str[idx]
    mid_point = 2 ** (level - 2)
    if position > mid_point:
        return get_character(level - 1, position - mid_point, idx, base_str).swapcase()
    return get_character(level - 1, position, idx, base_str)

def solve():
    base_string = input().strip()
    _ = int(input())
    query_positions = list(map(int, input().split()))
    length = len(base_string)

    output = []
    for pos in query_positions:
        pos -= 1  
        level = pos // length + 1  
        index = pos % length 
        output.append(get_character(61, level, index, base_string))
    
    return output

if __name__=="__main__":
    i = int(input())
    for _ in range(i):
        print(*(solve())) 
