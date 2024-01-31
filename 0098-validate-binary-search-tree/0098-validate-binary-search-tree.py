# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValidTree(node,left_val,right_val):
            if node==None:
                return True
            
            return (node.val>left_val and node.val<right_val) and (isValidTree(node.left,left_val,node.val)) and (isValidTree(node.right,node.val,right_val))
        
        
        return isValidTree(root,float("-inf"),float("inf"))