from collections import deque

class Node:
 def __init__(self,data):
  self.data=data
  self.left=None
  self.right=None

def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * level + prefix + str(root.data))
        if root.left or root.right:
            if root.left:
                print_tree(root.left, level + 2, "L--- ")
            if root.right:
                print_tree(root.right, level + 2, "R--- ")

#In Order DFS-Left-Root-Right
def in_order_dfs(node):
   if node is None:
      return
   in_order_dfs(node=node.left)
   print(node.data,end=' ')
   in_order_dfs(node=node.right)