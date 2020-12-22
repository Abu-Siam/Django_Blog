# Definition for singly-linked list.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0

        ResultList = ListNode(val=0, next=None)
        s1 = ""
        s2 = ""
        s3 = ""
        while (l1 is not None):
            s1 = str(l1.val) + s1
            l1 = l1.next
        while (l2 is not None):
            s2 = str(l2.val) + s2
            l2 = l2.next
        ans = int(s1) + int(s2)
        print(ans)
        temp = 1

        tempList = ListNode(val=0, next=None)
        while (True):

            ResultList.val = floor(ans / temp) - 10 * floor(ans / (temp * 10))
            if (temp == 1): tempList = ResultList
            temp = temp * 10
            print(ResultList.val)
            print(temp)
            if (ans % temp == ans):
                # ResultList=None
                ResultList = tempList

                break
            ResultList.next = ListNode(val=0, next=None)
            ResultList = ResultList.next

        return ResultList