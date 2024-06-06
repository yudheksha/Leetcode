# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def treeTraversal(root):
            
            nonlocal maxiHeight
            
            if not root:
                return 0
            
            leftHeight = treeTraversal(root.left)
            rightHeight = treeTraversal(root.right)
            
            maxiHeight = max(maxiHeight, leftHeight+rightHeight)
            
            return 1 + max(leftHeight,rightHeight)
        
        
        maxiHeight = 0
        treeTraversal(root)
        
        return maxiHeight
        