from collections import deque
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value): 
        if self.root is None:  
            self.root = TreeNode(value)
            return 

        cur = self.root 
        while True:
            if value < cur.value: 
                if cur.left is None: 
                    cur.left = TreeNode(value)
                    return 
                cur = cur.left
            if value > cur.value: 
                if cur.right is None: 
                    cur.right = TreeNode(value)
                    return 
                cur = cur.right 

def inorder(root):
    if root is None: 
        return
    inorder(root.left) 
    print(root.value)
    inorder(root.right)

def preorder(root):
    if root is None: 
        return
        
    print(root.value)
    preorder(root.left) 
    preorder(root.right)

def postorder(root): 
    if root is None: 
        return
        
    postorder(root.left) 
    postorder(root.right)
    print(root.value)


def levelorder(root): #BFS
    q = deque()
    level = 0

    if root: 
        q.append(root)

    while len(q) > 0:
        print(f"{level=}") 
        for _ in range(len(q)):
            cur = q.popleft()
            print(f"cur={cur.value}")
            if cur.left: 
                q.append(cur.left)
            if cur.right: 
                q.append(cur.right)
        level = level + 1
        
                    
if __name__ == '__main__': 
    bst = BinarySearchTree()
    for i in [4, 3, 6, 2, 5, 7]: 
        bst.insert(i)
        
    root = bst.root
           
    levelorder(root)            
