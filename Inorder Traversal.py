#Recursive Traversal:
class Solution:
    def inOrder(self, root):
        result = []
        self.traverse(root, result)
        return result

    def traverse(self, node, result):
        if node:
            self.traverse(node.left, result)  # Visit left subtree
            result.append(node.data)         # Visit node
            self.traverse(node.right, result) # Visit right subtree



#Iterative Inorder Traversal (Using a Stack)
class Solution:
    def inOrder(self, root):
        stack = []
        result = []
        current = root
        
        while current or stack:
            # Reach the leftmost Node
            while current:
                stack.append(current)
                current = current.left
            
            # Process the node at the top of the stack
            current = stack.pop()
            result.append(current.data)
            
            # Visit the right subtree
            current = current.right
        
        return result
