class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(nums,permutations,result,Hmap):
            if len(permutations) == len(nums):
                result.append(permutations.copy())
                return
            
            
            for i in range(len(nums)):
                if nums[i] not in Hmap:
                    Hmap[nums[i]] = True
                    permutations.append(nums[i])
                    dfs(nums,permutations,result,Hmap)
                    permutations.pop()
                    del Hmap[nums[i]]
                    
               
        permutations =[]
        result =[]
        Hmap ={}
        dfs(nums,permutations,result,Hmap)
        return result
                    
                    
                    
        