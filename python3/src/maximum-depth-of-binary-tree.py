# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        depth, maxDiff = self.recGetHeight(root)

        # print('depth:' + str(depth))
        # print('maxDiff:' + str(maxDiff))

        if maxDiff > 1:
            return False
        else:
            return True

    def recGetHeight(self, root: TreeNode) -> (int, int):
        if not root:
            return (0, 0)

        if not root.left:
            l = 0
            maxDiffL = 0
        else:
            l, maxDiffL = self.recGetHeight(root.left)
            l += 1

        if not root.right:
            r = 0
            maxDiffR = 0
        else:
            r, maxDiffR = self.recGetHeight(root.right)
            r += 1

        #         print('depth: ' + str(root.val) + ' left:' + str(l) + ' right:' + str(r))

        #         print(abs(maxDiffL-maxDiffR))
        #         print(abs(l-r))

        return max(l, r), max(abs(l - r), max(maxDiffL, maxDiffR))
