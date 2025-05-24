from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def depth(self, root):
        if root is None:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.isBalanced(root.left) and self.isBalanced(root.right) \
               and abs(self.depth(root.left) - self.depth(root.right)) < 2

    def buildTreeWithLayerOrder(self, seq):
        if len(seq) == 0:
            return None

        root = TreeNode(seq[0])
        nodes = [root]

        ptr = 1
        while len(nodes) > 0:
            n = nodes[0]
            nodes = nodes[1:]
            
            if ptr >= len(seq): break
            if seq[ptr] is not None:
                lhs = TreeNode(seq[ptr])
                n.left = lhs
                nodes.append(lhs)
            ptr += 1

            if ptr >= len(seq): break
            if seq[ptr] is not None:
                rhs = TreeNode(seq[ptr])
                n.right = rhs
                nodes.append(rhs)
            ptr += 1

        return root

    def test(self):
        table_test = [
           ( [3,9,20,None,None,15,7], True),
           ( [1,2,2,3,3,None,None,4,4], False),
           ([], True),
        ]

        for seq, label in table_test:
            root = self.buildTreeWithLayerOrder(seq)
            ret = self.isBalanced(root)

            print(f"excepted: {label}, actual: {ret}")
            assert ret == label


if __name__=="__main__":
    sol = Solution()
    sol.test()


