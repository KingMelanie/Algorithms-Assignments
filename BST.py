class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution():
    def recurMaxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_depth = self.recurMaxDepth(root.left)
        right_depth = self.recurMaxDepth(root.right)
        return max(left_depth, right_depth) + 1

    def iterMaxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        max_depth = 0
        while stack:
            node, depth = stack.pop()
            if not node.left and not node.right:
                max_depth = max(max_depth, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return max_depth

#1
#Input: root = [3,9,20,null,null,15,7]
#Output: 3   
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

S = Solution()

# Call the maxDepth function with the root of the binary tree
recursive_depth = S.recurMaxDepth(root)
print("Maximum depth of the first binary tree using recursion: ", recursive_depth)

# Call the maxDepth function with the root of the binary tree
iterative_depth = S.iterMaxDepth(root)
print("Maximum depth of the first binary tree using iteration: ", iterative_depth)

#2
#Input: root = [1,null,2]
#Output: 2

root = TreeNode(1)
root.right = TreeNode(2)

S = Solution()

# Call the maxDepth function with the root of the binary tree
recursive_depth = S.recurMaxDepth(root)
print("Maximum depth of the second binary tree using recursion: ", recursive_depth)

# Call the maxDepth function with the root of the binary tree
iterative_depth = S.iterMaxDepth(root)
print("Maximum depth of the second binary tree using iteration: ", iterative_depth)




