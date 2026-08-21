class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for ss in strs:
            s+=(ss)
            s+=("//xx")
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        strs = list()
        strs = s.split("//xx")
        strs.pop()
        return strs