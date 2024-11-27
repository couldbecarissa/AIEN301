import binarytree

root=binarytree.Node(2)
nodeOne=binarytree.Node(3)
nodeTwo=binarytree.Node(4)
nodeThree=binarytree.Node(5)
root.left=nodeOne
root.right=nodeTwo
root.left.left=nodeThree
print("To observe the tree in its natural form: ")
binarytree.print_tree(root)
print("In order DFS: ")
binarytree.in_order_dfs(root)
print("\nBreadth First Search:")
binarytree.bfs(root)
print("\nIs the number 8 present?")
if binarytree.searching(root,8)==True:
    print('Yes')
else:print("NAH")
print("\nHeight please:"+ str(binarytree.height(root)))