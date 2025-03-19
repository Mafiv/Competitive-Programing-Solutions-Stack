# Problem: Reveal Cards In Increasing Order - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        x = deque()
        for num in sorted(deck, reverse=True):
            if x:
                x.appendleft(x.pop())
            x.appendleft(num)
        return list(x)        