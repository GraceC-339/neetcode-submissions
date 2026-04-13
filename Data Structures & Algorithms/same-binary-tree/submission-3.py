# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # dfs iterative
        stack1 = [p]
        stack2 = [q]

        while stack1 and stack2:
            n1 = stack1.pop()
            n2 = stack2.pop()
            if not n1 and not n2:
                continue
            if not n1 or not n2 or n1.val != n2.val:
                return False
            stack1.extend([n1.left,n1.right])
            stack2.extend([n2.left, n2.right])
        
        return not stack1 and not stack2
