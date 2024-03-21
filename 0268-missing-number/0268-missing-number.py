class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        s= set(nums)
        
        n=len(s)+1
        for i in range(n):
            if i not in s:
                return i
            
            
            
        