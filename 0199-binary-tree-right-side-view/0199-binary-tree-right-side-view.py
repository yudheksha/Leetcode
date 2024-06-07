# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        
        def treeTraversal(root,level):
            
            if not root:
                return
            
            if len(rightView)==level:
                rightView.append(root.val)
                
            
            treeTraversal(root.right,level+1)
            treeTraversal(root.left,level+1)
                
        
        level = 0
        rightView = []
        
        treeTraversal(root,level)
        
        return rightView
        