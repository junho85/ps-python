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

    def list_to_num(self, ln):
        tmp = ln

        reversed_num_str = ""

        while tmp:
            reversed_num_str += str(tmp.val)
            tmp = tmp.next

        return int(reversed_num_str[::-1])

    def num_to_list(self, num):
        ln = ListNode(0)  # head node

        for n in str(num)[::-1]:
            self.append(ln, n)

        return ln.next

    def print(self, ln):
        tmp = ln

        while tmp:
            print(tmp.val, end="")
            tmp = tmp.next
        print()

    def addTwoNumbers(self, l1, l2):
        sum = self.list_to_num(l1) + self.list_to_num(l2)
        return self.num_to_list(sum)


s = Solution()

l1 = ListNode(2)
s.append(l1, 4)
s.append(l1, 3)

print(s.list_to_num(l1))
# s.print(l1)

l2 = ListNode(5)
s.append(l2, 6)
s.append(l2, 4)

print(s.list_to_num(l2))
# s.print(l2)

result = s.addTwoNumbers(l1, l2)
s.print(result)
