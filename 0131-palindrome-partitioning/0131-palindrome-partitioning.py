class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        
        
        def backtrack(index, s, partition, result):
            if index == len(s):
                result.append(partition.copy())
                return
            
            
            for i in range(index,len(s)):
                if s[index:i+1] == s[index:i+1][::-1]:
                    partition.append(s[index:i+1])
                    backtrack(i+1,s,partition,result)
                    partition.pop()
                    
        
        partition = []
        result = []
                    
        backtrack(0,s,partition, result)
        return result