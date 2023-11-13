class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(ransomNote) > len(magazine): return False

        hash_magazine = {}
        for item in magazine:
            if item not in hash_magazine:
                hash_magazine[item] = 1
            else:
                hash_magazine[item] += 1

        for note in ransomNote:
            if note not in hash_magazine:
                return False
            else:
                hash_magazine[note] -= 1
                if hash_magazine[note] < 0:
                    return False
        
        return True
        

            
        
