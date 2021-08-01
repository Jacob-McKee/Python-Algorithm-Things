# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        if cloned is None:
            return None

        queue = []

        queue.append(cloned)

        while len(queue) > 0:
            node = queue.pop(0)

            if node.val == target.val:
                return node

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)
