class Solution:
    def romanToInt(self, s: str) -> int:
        # declare of output integer
        output = 0
        # declare of two hashmap
        hashmap_basic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        hashmap_derived = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        
        # better use while
        for item in hashmap_derived.keys():
            # check if any key in it
            if item in s:
                output += hashmap_derived[item]
                s = s.replace(item,"",1)

        # 由于不存在特例了，直接iterate string就好
        for c in s:
            output += hashmap_basic[c]

        return output

            
        
        