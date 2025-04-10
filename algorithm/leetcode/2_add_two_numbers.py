# status: accepted

import os,sys
from typing import Optional 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        result = ListNode()
        ptr = result
        carry = 0
        while True:
            if l1 is None and l2 is None:
                break
            elif l1 is None:
                l1_val = 0
                l2_val = l2.val
                l2 = l2.next
            elif l2 is None:
                l2_val = 0
                l1_val = l1.val
                l1 = l1.next
            else:
                l1_val = l1.val
                l2_val = l2.val
                l1 = l1.next
                l2 = l2.next

            ptr.next = ListNode()
            ptr = ptr.next

            sum_val = l1_val + l2_val + carry
            ptr.val = sum_val % 10
            carry   = sum_val // 10

        if carry:
            ptr.next = ListNode(1)

        return result.next

    def benchmark(self):
        cases = [
            (
            self.convert_list_2_listnode([2, 4, 3]),
            self.convert_list_2_listnode([5, 6, 4]),
            self.convert_list_2_listnode([7, 0, 8])
            ),
            (self.convert_list_2_listnode([9, 9, 9, 9, 9, 9, 9]),
             self.convert_list_2_listnode([9, 9, 9, 9]),
             self.convert_list_2_listnode([8,9,9,9,0,0,0,1])
             )
        ]

        for case in cases:
            yield case


    def convert_list_2_listnode(self, l):
        list_node = ListNode()
        ptr = list_node

        for i in l:
            ptr.next = ListNode(i)
            ptr = ptr.next

        return list_node.next



    def print_list_node(self, l):
        print("list: ", end='')
        ptr = l
        while ptr is not None:
            print(f"{ptr.val} ", end='')
            ptr = ptr.next
        print()
                    
if __name__=="__main__":
    sol = Solution()
    for l1, l2, gt in sol.benchmark():
        sol.print_list_node(l1)
        sol.print_list_node(l2)
        l3 = sol.addTwoNumbers(l1, l2)
        sol.print_list_node(l3)
        sol.print_list_node(gt)
        print("--------------")

