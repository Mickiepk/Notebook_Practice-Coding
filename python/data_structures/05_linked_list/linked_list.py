class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def from_list(values):
    """Helper: [1, 2, 3] -> 1 -> 2 -> 3 -> None"""
    dummy = tail = ListNode()
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head):
    """Helper: 1 -> 2 -> 3 -> None  ->  [1, 2, 3]"""
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def add_two_numbers(l1, l2):
    """Digits are stored in reverse order. Return the sum as a new list in the same format."""
    raise NotImplementedError


def reverse_between(head, left, right):
    """Reverse nodes from position left to right (1-indexed, inclusive). Return the new head."""
    raise NotImplementedError
