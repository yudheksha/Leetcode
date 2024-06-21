# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def preorderBST(root1,root2):
            
            if not root1 and not root2 :
                return True
            
            if not root1 and root2 or not root2 and root1 :
                return False
            
            if root1.val != root2.val:
                return False
            
            return (preorderBST(root1.left,root2.left) and
            preorderBST(root1.right,root2.right))
            
            
        return preorderBST(p,q)