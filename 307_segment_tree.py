# leetcode 307: https://leetcode.com/problems/range-sum-query-mutable
# Build Tree Time: O(n)
# Update Time: O(logn)
# Find Range: O(logn + k)
# Space: O(n)

class SegmentTreeNode(object):
    def __init__(self, left, right, val, left_node=None, right_node=None):
        self.start = left
        self.end = right
        self.val = val
        self.left = left_node
        self.right = right_node

class NumArray(object):

    # T(n) = 2*T(n/2) = O(n)
    def build_tree(self, l, r):
        if l == r:
            return SegmentTreeNode(l, r, self.nums[l])
        mid = (l + r) >> 1
        left = self.build_tree(l, mid)
        right = self.build_tree(mid + 1, r)
        return SegmentTreeNode(l, r, left.val + right.val, left, right)

    # T(n) = T(n/2) + 1 = O(logn)
    def update_tree(self, node, i, val):
        if not node: return
        if node.start == node.end == i:
            node.val = val
            return
        elif ((node.start + node.end) >> 1) >= i:
            self.update_tree(node.left, i, val)
        else:
            self.update_tree(node.right, i, val)
        node.val = node.left.val + node.right.val

    # T(n) = T(n/2) + k, where k is the split time, T(n) in worst case is < O(n)
    def find_range(self, node, i, j):
        if not node: return 0
        if node.start == i and node.end == j:
            return node.val
        mid = (node.start + node.end) >> 1
        if i > mid:
            return self.find_range(node.right, i, j)
        elif j <= mid:
            return self.find_range(node.left, i, j)
        else:
            return self.find_range(node.left, i, mid) + self.find_range(node.right, mid+1, j)

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # build tree
        self.nums = nums
        self.root = self.build_tree(0, len(nums) - 1) if len(nums) else None


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self.update_tree(self.root, i, val)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.find_range(self.root, i, j)
    
