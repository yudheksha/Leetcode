class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(index,candidates,target, result,combination):
            if target ==0:
                result.append(combination.copy())
                return
            
            
            if target<0 or index==len(candidates):
                return
            
            if candidates[index]<=target:
                combination.append(candidates[index])
                dfs(index,candidates,target-candidates[index],result,combination)
                combination.pop()
                
                
            dfs(index+1, candidates, target,result,combination)
            
            
            
        result = []
        combination=[]
        dfs(0,candidates,target, result, combination)
        return result
            