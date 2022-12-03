class Solution:
    
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(0, n + 1):
            ans.append(self.countBitsInSingleNumber(i))
        
        return ans
        
    def countBitsInSingleNumber(self, n: int) -> int:
        num_bits = 0
        
        while n:
            num_bits += n & 1
            n >>= 1
            
        return num_bits
      
      
