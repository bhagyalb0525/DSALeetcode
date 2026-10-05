class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        freq={}
        for i in strs:
            sortedi="".join(sorted(i))
            if sortedi in freq:
                freq[sortedi].append(i)
            else:
                freq[sortedi]=[i]
        L=list(freq.values())
        return L