class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")

print(Solution().defangIPaddr("255.100.50.0"))