class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        x = [-num for num in gifts]
        heapify(x)
        while k:
            tmp = math.isqrt(-heappop(x))
            heappush(x, -tmp)
            k -= 1
            
        return -sum(x)



