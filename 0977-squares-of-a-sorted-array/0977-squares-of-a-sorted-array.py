class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            nums[i]=nums[i]**2
            
            
        n=len(nums)    
        head=0
        tail=n-1
        
        arr=[0]*n
        i=n-1
        while head<=tail:
            if nums[tail]>nums[head]:
                arr[i]=nums[tail]
                i-=1
                tail-=1
                
            else:
                arr[i]=nums[head]
                i-=1
                head+=1
                
                
        return arr
                
                
            