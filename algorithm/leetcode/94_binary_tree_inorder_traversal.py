from typing import Optional, List






# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
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


    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


    def test(self):
        test_table = [
            ([1,None,2,3], [1, 3, 2]),
            ([1,2,3,4,5,None,8,None,None,6,7,9], [4,2,6,5,7,1,3,9,8]),
            ([], []),
            ([1], [1]),
        ]


        for seq, label in test_table:
            root = self.buildTreeWithLayerOrder(seq)
            ret = self.inorderTraversal(root)

            print(f"excepted: {label}, actual: {ret}")
            assert ret == label


if __name__=="__main__":
    sol = Solution()
    sol.test()


