# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

# Always choose the word that has minimum zero-match with the other words
# since worst case, master.guess(word) would return 0
# then we only keep the words that have 0 overlap with the guessed word
# so we optimize on the worst case - always choose the ones has least num of zero matches
# thus we can prune the wordlist fastly.

class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        # time - O(n^2)
        # space - O(n)
        
        def match(a, b):
            cnt = 0
            for x, y in zip(a, b):
                if x == y:
                    cnt += 1
            return cnt
        
        for _ in xrange(10):
            c = collections.defaultdict(int)
        
            for w in wordlist:
                for x in wordlist:
                    if x == w: continue
                    if match(x, w) == 0:
                        c[w] += 1
            
            pair = (wordlist[0], 1000)
            for k, v in c.items():
                if v < pair[1]:
                    pair = (k, v)
            
            n = master.guess(pair[0])
            if n == 6: return
            
            curr = []
            for word in wordlist:
                if word == pair[0] or not match(word, pair[0]) == n: continue
                curr.append(word)
            wordlist = curr

