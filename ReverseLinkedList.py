#Definition for singly-linked list
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def nonrecurse(head):
    if head is None or head.next is None:
        return head
    pre, cur, h = None, head, head
    while cur:
        h = cur
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return h

# create 1 --> 2 --> 3 -->4 --> None
head, p1, p2, p3 = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
head.next = p1
p1.next = p2
p2.next = p3
# result: 4 --> 3 --> 2 --> 1 --> None
p = nonrecurse(head)
while p:
    print(p.val)
    p = p.next