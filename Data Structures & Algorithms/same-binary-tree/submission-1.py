# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        #some sort of recursion
        # if p but not q or not p but q, then false
        # if p and q then check value do that for every branch left and right
        if (p and not q) or (q and not p):
            return False
        elif not p and not q:
            return True
        elif p.val != q.val:
            return False
        elif p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        
        
        