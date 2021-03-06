
class Solution():
    
    def hasPairWithSumUnordered(self, data, sum): # time: O(n), space: O(n)
        compliments = set()
        for value in data:
            if value in compliments:
                return True
            
            compliments.add(sum - value)
            
        return False
    
    
    def hasPairWithSumOrdered(self, data, sum): # time: O(n), space: O(1) 
        lowBound = 0
        hiBound = len(data) - 1

        while lowBound < hiBound:
            _s = data[lowBound] + data[hiBound]
            if _s == sum:
                return True
            elif _s < sum:
                lowBound += 1
            else:
                hiBound -= 1
            
        return False

    
print(Solution().hasPairWithSumUnordered([1, 2, 3, 9], 8))
print(Solution().hasPairWithSumUnordered([1, 2, 4, 4], 8))


print(Solution().hasPairWithSumOrdered([1, 2, 3, 9], 8))
print(Solution().hasPairWithSumOrdered([1, 2, 4, 4], 8))