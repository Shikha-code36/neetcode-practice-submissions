class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res= {}

        for s in strs:
            count=[0]*26
            for ch in s:
                count[ord(ch)-ord('a')]+=1
            key=tuple(count)
            if key in res:
                res[key].append(s)
            else:
                res[key]=[s]
        return list(res.values())

        