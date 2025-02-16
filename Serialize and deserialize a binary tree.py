from collections import deque

class Solution:
    def serialize(self, root):
        """Serializes a binary tree to a list."""
        if not root:
            return []
        
        queue = deque([root])
        result = []
        
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.data)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append('N')  # Using 'N' for None
        
        return result

    def deSerialize(self, data):
        """Deserializes the list back to a binary tree."""
        if not data or data[0] == 'N':
            return None
        
        root = Node(data[0])
        queue = deque([root])
        i = 1  # Pointer for data array
        
        while queue and i < len(data):
            node = queue.popleft()
            
            if data[i] != 'N':
                node.left = Node(data[i])
                queue.append(node.left)
            i += 1
            
            if i < len(data) and data[i] != 'N':
                node.right = Node(data[i])
                queue.append(node.right)
            i += 1
        
        return root
