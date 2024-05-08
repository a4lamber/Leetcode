from collections import defaultdict


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # 1. create a hashmap, sort the hashmap based on val, then by key
        # 2. initialize an solution array with index:value being frequency:[val,val]
        # 3. populate the soluton array
        # 4. iterate the solution array while sort it on the fly
        hashmap = defaultdict(int)
        for word in words:
            hashmap[word] += 1

        frequency = [[] for _ in range(len(words) + 1)]

        for word, count in hashmap.items():
            frequency[count].append(word)

        res = []
        for i in range(len(frequency) - 1, 0, -1):
            if frequency[i]:
                # sort lexicographically
                frequency[i].sort()
                for val in frequency[i]:
                    res.append(val)
                    if len(res) == k:
                        return res
