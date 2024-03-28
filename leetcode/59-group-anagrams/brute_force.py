"""
 # @ Author: Adam
 # @ Create Time: 2024-01-23 21:07:57
 # @ Modified by: Adam
 # @ Modified time: 2024-01-23 21:08:10
 # @ Description: 感觉自己写的还不错，但是超时了
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initialization: the first element of strs will always be unique by itself (看子问题的角度)
        # build a helper function to check if two words are anagram
        # traverse the strs nested traversing res such that the anagram of any subarray in the res array, like
        # [["eat","ate"],["bat"]], you just need to pick "eat" from ["eat","ate"] and "bat" from ["bat"]

        def is_anagram(word_a, word_b):
            """take in two words, return T or F based on if two args are anagram"""
            hashtable = dict()
            for char in word_a:
                if char not in hashtable.keys():
                    hashtable[char] = 1
                else:
                    hashtable[char] += 1

            for char in word_b:
                if char in hashtable.keys():
                    hashtable[char] -= 1
                else:
                    # not
                    return False

            for i, value in hashtable.items():
                if value != 0:
                    return False

            return True

        # initialize the solution array
        res = [[strs[0]]]

        for i, word in enumerate(strs):
            if i == 0:
                continue

            counter = len(res)
            for j in range(len(res)):
                # 1st element of the resultant subarray
                if is_anagram(word, res[j][0]):
                    res[j].append(word)
                    break
                counter -= 1

            if counter == 0:
                # if reach here, it means we exhaust the potential solution and find a new unique anagram
                res.append([word])

        return res
