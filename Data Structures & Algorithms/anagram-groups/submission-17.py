from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hashmap = defaultdict(list)

        for word in strs:
            currCounter = Counter(word)
            arr = [0] * 26

            for letter in currCounter: 
                arr[ord(letter) - ord("a")] = currCounter[letter]

            hashmap[tuple(arr)].append(word)

        for key, arr in hashmap.items():
            res.append(arr)

        return res 

                
