# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None
        t3 = TreeNode()
        if t1 or t2:
            t3.val = (t1.val if t1 else 0 ) +  (t2.val if t2 else 0 )
            if not t1:
                t3.right = self.mergeTrees(t1, t2.right)
                t3.left = self.mergeTrees(t1, t2.left)
            elif not t2:
                t3.right = self.mergeTrees(t1.right , t2)
                t3.left = self.mergeTrees(t1.left, t2)
            else:
                t3.right = self.mergeTrees(t1.right , t2.right)
                t3.left = self.mergeTrees(t1.left, t2.left)
            
        return t3