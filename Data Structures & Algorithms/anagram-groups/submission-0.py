class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        glist = defaultdict(list)
        for s in strs: 
            S = ''.join(sorted(s))
            glist[S].append(s)
        return list(glist.values())