class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.same(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    def same(self,a,b):
        if not a and not b:
            return True
        if not a or not b or a.val!=b.val:
            return False
        return self.same(a.left,b.left) and self.same(a.right,b.right)

