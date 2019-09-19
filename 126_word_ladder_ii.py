class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        D = collections.defaultdict(list)
        for idx, word in enumerate(wordList):
            for i in xrange(len(word)):
                key = word[:i] + '*' + word[i+1:]
                D[key].append(idx)
        
        D_neighbor = collections.defaultdict(set)
        level = {beginWord: 0}
        visited = [False] * len(wordList)
        
        # bfs, from word ladder 1, to get min_len
        def getLen():
            q = collections.deque([beginWord])
            cnt = 0

            while q:
                cnt += 1
                l = len(q)
                for _ in xrange(l):
                    word = q.popleft()
                    if word == endWord:
                        return cnt
                    for i in xrange(len(word)):
                        key = word[:i] + '*' + word[i+1:]
                        for next in D[key]:
                            if wordList[next] != word: # add next level
                                D_neighbor[word].add(wordList[next])
                            if not visited[next]:
                                if not wordList[next] in level:
                                    level[wordList[next]] = cnt # level of first occurence
                                q.append(wordList[next])
                                visited[next] = True
            return 0
        
        self.min_len = getLen()
        self.ret = []
        
        # dfs go over the path
        def dfs(prev_list):
            if len(prev_list) == self.min_len and prev_list[-1] == endWord: self.ret.append(prev_list)
            if len(prev_list) >= self.min_len: return
            word = prev_list[-1]
            s = set()
            for next in D_neighbor[word]:
                if next in level and level[next] == level[word] + 1:
                    dfs(prev_list + [next])

        dfs([beginWord])
        
        return self.ret
