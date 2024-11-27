import binarytree

root=binarytree.Node(2)
nodeOne=binarytree.Node(3)
nodeTwo=binarytree.Node(4)
nodeThree=binarytree.Node(5)
root.left=nodeOne
root.right=nodeTwo
root.left.left=nodeThree
binarytree.print_tree(root)
binarytree.in_order_dfs(root)