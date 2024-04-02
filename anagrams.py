class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = {}

        for word in strs:
            key = ''.join(sorted(word))
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]

        result = list(anagrams.values())
        return result
        

#test case
#Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))

