def isPalindrome(self, head: ListNode) -> bool:
    def helper(start, end):
        if start > end:
            return True
        if li[start] != li[end]:
            return False
        return helper(start + 1, end - 1)

    li = []
    while head:
        li.append(head.val)
        head = head.next
    return helper(0, len(li) - 1)
