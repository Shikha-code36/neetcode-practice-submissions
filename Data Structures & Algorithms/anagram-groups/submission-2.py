class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        seen={}
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if key in seen:
                seen[key].append(strs[i])
            else:
                seen[key]=[strs[i]]
        
        res=list(seen.values())

        return res
            

            

        