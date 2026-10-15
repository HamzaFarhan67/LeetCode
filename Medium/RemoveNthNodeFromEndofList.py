# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def removeNthFromEnd(self, head, n):
        count=0
        temp=head
        while temp is not None:
            count+=1
            temp=temp.next
        count= count-n
        if count==0:
            return head.next
        ntemp=head
        while count >1:
            count -=1
            ntemp= ntemp.next
        
        ntemp.next=ntemp.next.next
        return head
