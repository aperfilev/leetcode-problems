
class Solution():
    
    def getAllPermutations(self, input):
        result = []
        transmutation = []
        rest = input.copy()
        
        self.recSearch(result, transmutation, rest)
        
        return result


    def recSearch(self, result, transmutation, rest):
        if len(rest) == 0:
            result.append(transmutation)
        
        for i in range(0, len(rest)):
            _rest = rest.copy()
            n = _rest.pop(i)
            _transmutation = transmutation.copy()
            _transmutation.append(n)
            
            self.recSearch(result, _transmutation, _rest)


input = [1, 2, 3, 4]
print(Solution().getAllPermutations(input))
#[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]