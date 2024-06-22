# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        
        def preorderBT(node, gtVal):
            nonlocal count
            
            if not node:
                return
            
            if node.val>=gtVal:
                gtVal = node.val
                count+=1
                
                
            preorderBT(node.left,gtVal)
            preorderBT(node.right,gtVal)
            
            
        count = 0   
        preorderBT(root,float("-inf"))
        return count
        