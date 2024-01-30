# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        output=[]
        res=[]
        
        q=deque()
        
        q.append(root)
        q.append(None)
        
        while len(q)>1:
            
            curr=q.popleft()
            
            if curr==None:
                output.append(res)
                res=[]
                q.append(None)
                continue
                
            res.append(curr.val)
            
            if curr.left!=None:
                q.append(curr.left)
                
            if curr.right!=None:
                q.append(curr.right)
            
            
        output.append(res)
        return output
            
            
        