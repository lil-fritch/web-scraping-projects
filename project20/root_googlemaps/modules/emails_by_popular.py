import re
from typing import List

import requests

class EmailExtractor:
    def __init__(self, domains: List[str]):
        self.domains = domains
        self.domain_pattern = "|".join(re.escape(domain) for domain in domains)
        self.email_pattern = rf"[a-zA-Z0-9._%+-]+(?:{self.domain_pattern})"

    def extract(self, text: str) -> List[str]:
        print('Extracting emails (method 1)')
        emails = re.findall(self.email_pattern, text)
        if len(emails) == 1:
            return emails[0]
        return list(set(emails))