class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for email in emails:
            name, domain = email.split('@')
            name = name.split('+')[0].replace('.', '')
            s.add(name + '@' + domain)
        return len(s)