# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and
                   self.sameTree(root.right, subRoot.right))
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        q = [root]
        while q:
            curr = q.pop(0)
            print(curr.left, subRoot.left)
            if self.sameTree(curr, subRoot):
                return True
            else:
                if curr.left != None:
                    q.append(curr.left)
                if curr.right != None:
                    q.append(curr.right)
        
        return False