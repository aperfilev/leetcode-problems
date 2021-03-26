class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        output = []
        for word in reversed(words):
            output.append(word)

        return " ".join(output)


print(Solution().reverseWords("the sky is blue")) # "blue is sky the"
