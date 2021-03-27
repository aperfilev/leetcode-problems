from typing import List

class Node():
    def __init__(self, val):
        self.val = val
        self.children = dict()
        self.empty = False

    def update(self, word):
        if len(word) == 0:
            self.empty = True
            return

        if word[0] not in self.children:
            self.children[word[0]] = Node(word[0])

        node = self.children[word[0]]
        node.update(word[1:])

    def getLCP(self):

        node = self
        prefix = ""
        while len(node.children) == 1 and not node.empty:
            key = list(node.children.keys())[0]
            prefix += key
            node = node.children[key]

        return prefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Node("")

        for line in strs:
            trie.update(line)

        return trie.getLCP()




print("'{}'".format(Solution().longestCommonPrefix(["flower","flow","flight"]))) #fl
print("'{}'".format(Solution().longestCommonPrefix([""])))
print("'{}'".format(Solution().longestCommonPrefix([" "])))
print("'{}'".format(Solution().longestCommonPrefix(["","b"])))

