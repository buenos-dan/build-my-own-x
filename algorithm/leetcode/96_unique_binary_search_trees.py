"""
algo: DP
"""

from typing import Optional, List


class Solution:

    # nodes:  0  1  2  3 ...     
    ans =    [1, 1, 2, 5]

    def numTrees(self, n: int) -> int:
        if n < len(self.ans):
            return self.ans[n]

        self.ans.append(sum([ self.numTrees(i) * self.numTrees(n-i-1) for i in range(n)]))

        return self.ans[n]


    def test(self):
        test_table = [
            (3, 5),
            (1, 1),
            (4, 14),
        ]

        for n, label in test_table:
            ret = self.numTrees(n)
            
            print(f"excepted: {label}, actual: {ret}")
            assert ret == label



if __name__=="__main__":
    sol = Solution()
    sol.test()



