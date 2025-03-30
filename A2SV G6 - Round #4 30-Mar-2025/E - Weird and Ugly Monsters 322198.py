# Problem: E - Weird and Ugly Monsters - https://codeforces.com/gym/590053/problem/E

class ListNode:
    def __init__(self, index, ugliness):
        self.index = index
        self.ugliness = ugliness
        self.next = self.prev = None


def merge(node, count):
    while True:
        merged = False
        
        # Merge with the left neighbor
        if node.prev != node and node.ugliness == node.prev.ugliness:
            left = node.prev
            if node.index > left.index:
                left.next = node.next
                node.next.prev = left
                left.ugliness *= 2
                count[0] -= 1
                node = left
            else:
                node.prev = left.prev
                left.prev.next = node
                node.ugliness *= 2
                count[0] -= 1
            merged = True
        
        # Merge with the right neighbor
        elif node.next != node and node.ugliness == node.next.ugliness:
            right = node.next
            if node.index > right.index:
                node.prev.next = right
                right.prev = node.prev
                right.ugliness *= 2
                count[0] -= 1
                node = right
            else:
                right.next.prev = node
                node.next = right.next
                node.ugliness *= 2
                count[0] -= 1
            merged = True
        
        if not merged:
            break


def solve():
    num_insertions, initial_ugliness = map(int, input().split())
    count = [1]
    head = ListNode(1, initial_ugliness)
    head.next = head.prev = head
    monster_map = {1: head}
    indices = list(map(int, input().split()))
    ugliness_values = list(map(int, input().split()))
    results, next_index = [], 2

    for i in range(num_insertions):
        monster = monster_map[indices[i]]
        new_monster = ListNode(next_index, ugliness_values[i])
        next_index += 1
        
        new_monster.next, new_monster.prev = monster.next, monster
        monster.next.prev = new_monster
        monster.next = new_monster
        monster_map[new_monster.index] = new_monster
        count[0] += 1
        
        merge(new_monster, count)
        results.append(count[0])
    
    print(*results)


for _ in range(int(input())):
    solve()
