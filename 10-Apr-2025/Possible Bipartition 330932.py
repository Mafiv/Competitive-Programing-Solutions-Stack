# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        color = [-1] * (n + 1)
        graph = defaultdict(list)

        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    if not dfs(neighbor):
                        return False
                elif color[neighbor] == color[node]:
                    return False
            return True

        for i in range(1, n + 1):
            if color[i] == -1:
                color[i] = 0
                if not dfs(i):
                    return False

        return True
