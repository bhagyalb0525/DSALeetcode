class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={}
        for i in strs:
            key=tuple(sorted(i))
            if key not in dict1:
                dict1[key]=[i]
            else:
                dict1[key].append(i)
        return list(dict1.values())
        