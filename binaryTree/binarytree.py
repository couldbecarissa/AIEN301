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

#Pre Order DFS(Root-Left-Right)
def pre_order_dfs(node):
   if node is None:
    return
   print(node.data,end=' ')
   pre_order_dfs(node.left)
   pre_order_dfs(node.right)

#Post Order DFS(Left-RIGHT-Root)
def post_order_dfs(node):
   if node is None:
    return
   post_order_dfs(node.left)
   post_order_dfs(node.right)
   print(node.data,end=' ')

#Level Ordered BFS
def bfs(node):
   if node is None:
    return
   queue=[node]
   while queue:
    node=queue.pop(0)
    print(node.data,end=' ')
    if node.left:
       queue.append(node.left)
    if node.right:
       queue.append(node.right)
    

#Inserting a Node to the tree
def insert_node(root,data):
   if root is None:
      return Node(data)
   else:
      queue=deque([root])
      while queue:
         node=queue.popleft()
         if node.left is None:
            node.left=Node(data)
            break
         else:queue.append(node.left)

         if node.right is None:
            node.right=Node(data)
            break
         else:queue.append(node.right)
   return root

#Searching in A Binary Tree
def searching(root,val):
   if root is None:
      return False
   if root.data==val:
      return True
   return searching(root.left,val) or searching(root.right,val)

#To obtain the height of the Binary Tree
def height(root):
   if root is None:
      return -1
   lHeight=height(root.left)
   rHeight=height(root.right)
   return max(rHeight,lHeight)+1