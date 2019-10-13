class Node(object):
    def __init__(self, val):
        self.left_cnt = 0
        self.cnt = 1
        self.val = val
        self.left = None
        self.right = None

# Time: O(nlogn) (when balanced BST)
# Space: O(n)
class SolutionBinarySearchTree(object):
     def _insert(self, val):
         # return smaller cnts
         # sum all the left_cnt of the path
         node = self.root
         cnt = 0
         while node:
             if val == node.val:
                 node.cnt += 1
                 cnt += node.left_cnt
                 break
             elif val > node.val:
                 cnt += node.left_cnt + node.cnt
                 if node.right:
                     node = node.right
                 else:
                     node.right = Node(val)
                     break
             else:
                 node.left_cnt += 1
                 if node.left:
                     node = node.left
                 else:
                     node.left = Node(val)
                     break
         return cnt
    
     def countSmaller(self, nums):
         """
         :type nums: List[int]
         :rtype: List[int]
         """
         if not nums: return []
         self.root = Node(nums.pop())
         ret = [0]
         while nums:
             ret.append(self._insert(nums.pop()))
         return ret[::-1]


# Time: O(nlogn)
# Space: O(n)
class SolutionMergeSortCounter(object):
    ### Solution 2 - merge sort (stabled)
    # count the number of right jump to left for each position
    def countSmaller(self, nums):
        if not nums: return []
        smaller = [0] * len(nums)
        
        def sort(enum):
            if len(enum) <= 1: return enum
            left, right = sort(enum[:len(enum)/2]), sort(enum[len(enum)/2:])
            m, n = len(left), len(right)
            i, j = 0, 0
            while i < m or j < n:
                if j == n or i < m and left[i][1] <= right[j][1]:
                    enum[i + j] = left[i]
                    smaller[left[i][0]] += j
                    i += 1
                else:
                    enum[i + j] = right[j]
                    j += 1
            return enum
        
        sort(list(enumerate(nums)))
        return smaller

