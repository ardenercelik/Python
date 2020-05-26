#leetcode 563

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
            
    def findTilt(self, root: TreeNode) -> int:
        self.ans = 0 
        def _sum(root):
            if not root:
                return 0
            
            if root:
                left = _sum(root.left)
                right = _sum(root.right)
                self.ans += abs(left-right)
                return root.val + left + right
        
        _sum(root)
        return self.ans
        