class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(index,candidates,target,combination,result):
            
            if target == 0:
                result.append(combination.copy())
                return
            
            for i in range(index,len(candidates)):
                if i>index and candidates[i]==candidates[i-1]:
                    continue
                    
                if candidates[i]>target:
                    return
                    
                combination.append(candidates[i])
                backtrack(i+1,candidates,target-candidates[i],combination,result)
                combination.pop()
                
                
           
        
        combination =[]
        result =[]
        candidates.sort()
        backtrack(0,candidates,target,combination, result)
        return result
                
                
        