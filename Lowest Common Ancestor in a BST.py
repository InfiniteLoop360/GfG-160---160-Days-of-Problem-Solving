class Solution:
    def LCA(self, root, n1, n2):
        # Base case
        if root is None:
            return None
        
        # If both n1 and n2 are smaller than root, LCA lies in left subtree
        if n1.data < root.data and n2.data < root.data:
            return self.LCA(root.left, n1, n2)
        
        # If both n1 and n2 are greater than root, LCA lies in right subtree
        if n1.data > root.data and n2.data > root.data:
            return self.LCA(root.right, n1, n2)
        
        # If root is between n1 and n2, root is the LCA
        return root
