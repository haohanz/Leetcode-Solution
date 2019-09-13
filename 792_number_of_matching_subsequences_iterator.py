#class TrieNode(object):
#    def __init__(self, isTerminal=0):
#        self.isTerminate = 0
#        self.next = [None] * 26

class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        ### Solution 1 - use trie - TLE
        # Time: O(sum(words[i].length + size(trie))

        ### Solution2 - lazy trie, use iterator
        # Time: O(sum(words[i].length) + S.length)
        # Space: O(words.length)
        D = collections.defaultdict(list)
        for it in map(iter, words):
            D[next(it)].append(it)
        for c in S:
            for it in D.pop(c, []):
                D[next(it, None)].append(it)
        return len(D[None])
