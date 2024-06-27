class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        L, R = 0,1
        maxProfit = 0
        
        while R < len(prices):
            
            if prices[L]> prices[R]:
                L=R
            else:
                maxProfit = max(maxProfit, prices[R] - prices[L])
            R+=1
            
            
        return maxProfit
                
                
            
                
                
            
            