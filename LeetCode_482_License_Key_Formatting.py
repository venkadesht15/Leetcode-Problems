class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        first_len=len(s) % k
        parts=[]
        if first_len>0:
            parts.append(s[:first_len])
        for i in range(first_len,len(s),k):
            parts.append(s[i:i+k])
        return "-".join(parts)



