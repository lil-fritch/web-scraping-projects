from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_launcher import SeleniumDriver
from typing import Dict

class SocialLinksExtractor:
    def __init__(self, driver: WebDriver):
        """
        Initialize the SocialLinksExtractor with a Selenium WebDriver instance.
        """
        self.driver = driver

    def extract_links(self) -> Dict[str, set]:
        """
        Extract social media links using XPath for each platform.
        """
        print('Extracting social links')
        social_links = {
            "facebook": self._extract_facebook_links(),
            "instagram": self._extract_instagram_links(),
            "linkedin": self._extract_linkedin_links(),
            "youtube": self._extract_youtube_links(),
            "x": self._extract_x_links(),
        }
        return social_links

    def _extract_links_by_xpath(self, xpath_pattern: str) -> set:
        """
        Generic method to extract links based on an XPath pattern.
        """
        links = set()
        elements = self.driver.find_elements(By.XPATH, xpath_pattern)
        for element in elements:
            href = element.get_attribute("href")
            if href:
                links.add(href)
        if not links:
            return None
        else:
            return links.pop()

    def _extract_facebook_links(self) -> set:
        """
        Extract Facebook links using XPath.
        """
        xpath = "//a[contains(@href, 'facebook.com')]"
        return self._extract_links_by_xpath(xpath)

    def _extract_instagram_links(self) -> set:
        """
        Extract Instagram links using XPath.
        """
        xpath = "//a[contains(@href, 'instagram.com')]"
        return self._extract_links_by_xpath(xpath)

    def _extract_linkedin_links(self) -> set:
        """
        Extract LinkedIn links using XPath.
        """
        xpath = "//a[contains(@href, 'linkedin.com')]"
        return self._extract_links_by_xpath(xpath)

    def _extract_youtube_links(self) -> set:
        """
        Extract YouTube links using XPath.
        """
        xpath = "//a[contains(@href, 'youtube.com')]"
        return self._extract_links_by_xpath(xpath)

    def _extract_x_links(self) -> set:
        """
        Extract Twitter/X links using XPath.
        """
        xpath = "//a[contains(@href, 'twitter.com') or contains(@href, 'x.com')]"
        return self._extract_links_by_xpath(xpath)