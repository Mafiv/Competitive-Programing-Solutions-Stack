class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            counts = []
            for s in strs:
                c = Counter(s)
                counts.append((c['0'], c['1']))
            for zeros, ones in counts:
                for i in range(m, zeros - 1, -1):
                    for j in range(n, ones - 1, -1):

                        dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
            return dp[m][n]
