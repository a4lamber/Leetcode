class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        # dictionary 储存特殊keyboard的location
        # do ittttttt!
        
        keyHash = {}
        
        for keyIndex, key in enumerate(keyboard):
            keyHash[key] = keyIndex

        totalDistanceKeyTraveled = 0

        # 俩指针，一个指向lastKey, 一个指向nextKey
        prev = 0
        curr = 0

        # traverse the word
        for i in range(len(word)):
            curr = keyHash[word[i]]

            totalDistanceKeyTraveled += abs(curr - prev)

            prev = curr
        
        return totalDistanceKeyTraveled
            