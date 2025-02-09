# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = ['' for _ in range(len(s))]
        for i, char in enumerate(s):
            ans[indices[i]] = char  # Now with a normal space
        return "".join(ans)