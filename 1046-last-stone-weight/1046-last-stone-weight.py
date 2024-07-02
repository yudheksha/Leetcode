class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]
        
        heapq.heapify(stones)
        
        while len(stones)>1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            
            if second > first:
                new_weight = first - second
            
                heapq.heappush(stones, new_weight)
            
        stones.append(0)   
        return abs(stones[0])