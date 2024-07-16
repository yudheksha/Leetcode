class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(index,nums,subset,result):
            result.append(subset.copy())
            
            for i in range(index,len(nums)):
                if i>index and nums[i]== nums[i-1]:
                    continue
                    
                subset.append(nums[i])
                backtrack(i+1,nums,subset,result)
                subset.pop()
                
                
                
        subset=[]
        result =[]
        nums.sort()
        backtrack(0,nums,subset,result)
        return result
                