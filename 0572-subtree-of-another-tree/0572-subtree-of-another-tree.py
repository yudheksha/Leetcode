# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def preOrderTraversal(r):
            
            if r==None:
                return "Null"
            
            return "^"+str(r.val)+preOrderTraversal(r.left)+preOrderTraversal(r.right)
        
        
        full_tree=preOrderTraversal(root)
        sub_tree=preOrderTraversal(subRoot)
        
        return sub_tree in full_tree
        
        