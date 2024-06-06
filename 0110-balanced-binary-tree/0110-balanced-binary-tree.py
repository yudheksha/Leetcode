# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def treeTraversal(root):
            
            if not root:
                return 0
            
            
            leftHeight = treeTraversal(root.left)
            
            rightHeight = treeTraversal(root.right)
            
            if leftHeight == -1 or rightHeight == -1:
                return -1
            
            if abs(rightHeight-leftHeight)>1:
                return -1
            
            return 1+max(leftHeight,rightHeight)
        
        return treeTraversal(root)!=-1    
            