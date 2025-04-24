from math import log2, ceil
from typing import List
import sys

input = sys.stdin.readline

class SegmentNode:
    def __init__(self, value=None):
        if value is not None:
            self.first = self.last = value
            self.length = self.prefix_len = self.suffix_len = 1
        else:
            self.first = self.last = 0
            self.length = self.prefix_len = self.suffix_len = 0

    @staticmethod
    def merge(left, right):
        if left.length == 0:
            return right
        if right.length == 0:
            return left

        merged = SegmentNode()
        merged.first = left.first
        merged.last = right.last

        if left.prefix_len == left.length and left.last <= right.first:
            merged.prefix_len = left.length + right.prefix_len
        else:
            merged.prefix_len = left.prefix_len

        if right.suffix_len == right.length and left.last <= right.first:
            merged.suffix_len = right.length + left.suffix_len
        else:
            merged.suffix_len = right.suffix_len

        merged.length = max(left.length, right.length)
        if left.last <= right.first:
            merged.length = max(merged.length, left.suffix_len + right.prefix_len)

        return merged


class SegmentTree:
    def __init__(self, array: List[int]) -> None:
        self.n = len(array)
        self.size = 1 << ceil(log2(self.n))
        self.tree = [SegmentNode() for _ in range(2 * self.size)]

        for i in range(self.n):
            self.tree[self.size + i] = SegmentNode(array[i])

        for i in range(self.size - 1, 0, -1):
            self.tree[i] = SegmentNode.merge(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, pos: int, value: int):
        pos += self.size
        self.tree[pos] = SegmentNode(value)
        i = pos // 2
        while i >= 1:
            self.tree[i] = SegmentNode.merge(self.tree[2 * i], self.tree[2 * i + 1])
            i //= 2

    def max_amount(self, left: int, right: int) -> int:
        left += self.size
        right += self.size
        res_left = SegmentNode()
        res_right = SegmentNode()

        while left <= right:
            if left % 2 == 1:
                res_left = SegmentNode.merge(res_left, self.tree[left])
                left += 1
            if right % 2 == 0:
                res_right = SegmentNode.merge(self.tree[right], res_right)
                right -= 1
            left //= 2
            right //= 2

        result = SegmentNode.merge(res_left, res_right)
        return result.length


n = int(input())
array = list(map(int, input().split()))
q = int(input())

tree = SegmentTree(array)

for _ in range(q):
    parts = list(map(int, input().split()))
    if parts[0] == 1:
        print(tree.max_amount(parts[1] - 1, parts[2] - 1))
    elif parts[0] == 2:
        tree.update(parts[1] - 1, parts[2])
