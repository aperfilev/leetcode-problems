from typing import List


class Solution:

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        # Step 1. Fetch Words
        prepraredLines = []
        candidatLine = []
        while len(words) > 0:
            candidatLine.append(words[0])
            if self.getMinimalLineWidth(candidatLine) <= maxWidth:
                # accept and continue fetching
                words.pop(0)
            else:
                candidatLine.pop(len(candidatLine) - 1) #remove last word

                if len(candidatLine) == 0:
                    raise Exception("Couldn't format string: single word too long")

                prepraredLines.append(candidatLine)
                candidatLine = []

        # dump remaining words
        prepraredLines.append(candidatLine)

        # Step 2. Push Spaces
        formattedLines = []
        for i in range(len(prepraredLines)):
            prepraredLine = prepraredLines[i]
            line = ""
            if len(prepraredLine) == 1 or i == len(prepraredLines) - 1:
                line = self.leftJustify(prepraredLine, maxWidth)
            else: # len(prepraredLine) > 1:
                gaps = [" "] * (len(prepraredLine) - 1)
                spacesCount = len(gaps)

                totalLeftSpaces = maxWidth
                totalLeftSpaces -= spacesCount

                charsCount = 0
                for word in prepraredLine:
                    charsCount += len(word)

                totalLeftSpaces -= charsCount

                pos = 0
                for i in range(totalLeftSpaces):
                    gaps[pos] += " "
                    pos += 1
                    pos = pos % len(gaps)

                line = self.joinWordsWithGaps(prepraredLine, gaps)

            formattedLines.append(line)

        return formattedLines

    def leftJustify(self, words, maxWidth):
        line = ""
        if len(words) > 0:
            line += words[0]

            for i in range(1, len(words)):
                line += " "
                line += words[i]

            for i in range(maxWidth - len(line)):
                line += " "

        return line


    def getMinimalLineWidth(self, words):
        width = 0
        if len(words) > 0:
            width += len(words[0])
            for i in range(1, len(words)):
                width += 1
                width += len(words[i])

        return width

    def joinWordsWithGaps(self, words, gaps):
        line = ""
        if len(words) == 1:
            line += words[0]
            line += gaps[0]
        elif len(words) > 1:
            line += words[0]
            for i in range(1, len(words)):
                line += gaps[i - 1]
                line += words[i]

        return line

#print(Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print(Solution().fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
#print(Solution().fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))


