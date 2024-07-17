class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1:
            return 1
        trust_map = {}
        for a,b in trust:
            trust_map[b] = trust_map.get(b,0) + 1
        
        winner = -1
        for k,v in trust_map.items():
            if v == n-1:
                winner = k
        if winner != -1:
            present = False
            for a,b in trust:
                if a == winner:
                    present = True
            if not present:
                return winner
            else:
                return -1
        else:
            return -1
            
        
        