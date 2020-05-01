""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def isBST(root, min, max):
    if root is None:
        return True
    if root.data <= min or root.data >= max:
        return False
    return isBST(root.left, min, root.data) and isBST(root.right, root.data, max)

def checkBST(root):
    return isBST(root, float('-inf'), float('inf'))
        
    