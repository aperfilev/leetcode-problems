class Solution():
    
    def firstPos(self, array, x):
        n = len(array)
        result = n
        low = 0
        high = n - 1
        while(low <= high):
            mid = low + int((high - low) / 2)
            if array[mid] >= x:
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return result
    
    def searchRange(self, array, x):
        first = self.firstPos(array, x)
        last = self.firstPos(array, x + 1) - 1
        
        if first <= last:
            return (first, last)
        
        return (-1, -1)


array = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 12, 13, 15]
print(Solution().searchRange(array, 8))
#(7, 10)
