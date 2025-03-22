from bs4 import BeautifulSoup
from typing import List
import requests

class MailtoEmailExtractor:
    def __init__(self, html_content: str):
        """
        Initialize the extractor with HTML content.
        """
        self.soup = BeautifulSoup(html_content, "html.parser")

    def find_emails(self) -> List[str]:
        """
        Find all email addresses linked with mailto: in the HTML.
        """
        print('Extracting emails (method 2)')
        emails = set()
        mailto_links = self.soup.find_all("a", href=True)

        for link in mailto_links:
            href = link.get("href")
            if href and href.startswith("mailto:"):
                email = href[7:]  # Remove "mailto:" prefix
                email = email.split("?")[0]
                if email:
                    emails.add(email)
        if len(emails) == 1:
            return list(emails)[0]
        return list(emails)

