class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        maxHeap = [ -freq for freq in count.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        q = deque()
        
        while maxHeap or q:
            time+=1
            
            if maxHeap:
                freq = 1+heapq.heappop(maxHeap)
                if freq:
                    q.append([freq, time+n])
                    
                    
            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])
                
        return time