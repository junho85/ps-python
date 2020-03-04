class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def append(self, ln, val):
        tmp = ln

        while tmp.next:
            tmp = tmp.next

        tmp.next = ListNode(val)

    def print(self, ln):
        tmp = ln

        while tmp:
            print(tmp.val, end="")
            tmp = tmp.next
        print()

    def addTwoNumbers(self, l1, l2):
        ln = ListNode(0)  # head node

        is_up = False

        while True:
            l1val = 0
            l2val = 0

            if l1 is not None:
                l1val = l1.val
                l1 = l1.next

            if l2 is not None:
                l2val = l2.val
                l2 = l2.next

            sum = l1val + l2val
            if is_up == True:
                sum += 1
                is_up = 0

            if sum >= 10:
                is_up = 1
                sum %= 10

            self.append(ln, sum)

            if l1 is not None or l2 is not None:
                continue

            break

        if is_up == 1:
            self.append(ln, 1)

        return ln.next


s = Solution()

l1 = ListNode(2)
s.append(l1, 4)
s.append(l1, 3)

s.print(l1)

l2 = ListNode(5)
s.append(l2, 6)
s.append(l2, 4)

s.print(l2)

result = s.addTwoNumbers(l1, l2)
s.print(result)
