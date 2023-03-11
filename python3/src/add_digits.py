#258 Add Digits
# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

class Solution(object):
    def addDigits1(self, num):
        """
        :type num: int
        :rtype: int
        """

        if num == 0: return 0
        if num % 9 == 0: return 9
        return num % 9

    def addDigits2(self, num):
        """
        :type num: int
        :rtype: int
        """
        list_num = list(str(num))
        while len(list_num) > 1:
            list_num = list(str(sum(int(el) for el in list_num)))
        return list_num[0]
