class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        output = address.replace(".","[.]")
        
        return output