from typing import List
import re

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:

        output = set()

        numbers = re.split('-|\\+|\\*', input)
        operators = list(filter(None, re.split('[0-9]+', input)))

        self.recEval(numbers, operators, output)

        output = list(output)

        for i in range(len(output)):
            output[i] = eval(output[i])

        output.sort()
        return output

    def recEval(self, nums, ops, output):
        if len(nums) == 1:
            output.add(nums[0])

        for i in range(len(nums) - 1):
            _nums = nums.copy()
            _ops = ops.copy()

            lv = _nums.pop(i)
            rv = _nums.pop(i)
            op = _ops.pop(i)
            value = '(' + str(lv) + op + str(rv) + ')'
            _nums.insert(i, value)

            self.recEval(_nums, _ops, output)



#print(Solution().diffWaysToCompute("2-1-1")) #[0, 2]
print(Solution().diffWaysToCompute("2*3-4*5")) #[-34, -14, -10, -10, 10]

