class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        output=[]
        s= set(nums)
        n=len(nums)+1
        
        for i in range(1,n):
            
            if i not in s:
                output.append(i)
                
                
        return output
            