class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        max_l = -1

        for length in range(1, n + 1):
            freq = {}

            for i in range(n - length + 1):
                sub = s[i:i + length]

                if all(c == sub[0] for c in sub):
                    freq[sub] = freq.get(sub, 0) + 1
                    if freq[sub] >= 3:
                        max_l = max(max_l, length)

        return max_l


        