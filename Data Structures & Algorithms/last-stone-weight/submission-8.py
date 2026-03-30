class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        l = []
        
        for n in stones:
            heapq.heappush(l,n)
        heapq.heapify_max(l)
        print(l)
        while len(l) > 1:
            heapq.heapify_max(l)
            maxi = heapq.nlargest(2, l)
            print(maxi)
            if maxi[0] == maxi[1]:
                heapq.heappop_max(l)
                heapq.heappop_max(l)
            else:
                heapq.heappop_max(l)
                heapq.heappop_max(l)
                heapq.heappush(l,maxi[0] - maxi[1])
        if l == []:
            return 0
        return max(l)
        
         