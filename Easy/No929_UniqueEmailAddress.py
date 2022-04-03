class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for i, v in enumerate(emails):
            v = v.split("@")
            if v[0].find("+") != -1:
                v[0] = v[0][:v[0].find("+")]
            v[0] = v[0].replace(".", "")
            emails[i] = "@".join(v)
        return len(set(emails))
        
            
                