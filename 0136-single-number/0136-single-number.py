class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        freq = dict()
        
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0)+1
            
            
        for key,val in freq.items():
            if val == 1:
                return key
            
            
