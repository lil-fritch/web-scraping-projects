from time import sleep
from selenium_launcher import SeleniumDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

class AboutCollector:
    def __init__(self, driver):
        """Initialize AboutCollector with a Selenium driver."""
        self.driver = driver
        
    def collect_about(self):
        
        print('Start scraping about')
        
        """Collect 'About' information by extracting categories and their elements using precise XPath."""
        try:
            # Open the ‘About’ tab
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//button[@role='tab' and contains(@aria-label, 'About')]",
                    )
                )
            ).click()
            sleep(2)

            # Find the main container with the ‘About’ information
            about_section = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//div[contains(@class, 'm6QErb DxyBCb kA9KIf dS8AEf XiKgde')]",
                    )
                )
            )

            # Find all category headings (<h2> elements)
            categories = about_section.find_elements(By.XPATH, ".//h2")
            about_info = []

            for category in categories:
                category_name = category.text.strip()
                if not category_name:
                    continue

                # Looking for items belonging to the current category
                ul_element = category.find_element(
                    By.XPATH, "./following-sibling::ul[1]"
                )
                items = ul_element.find_elements(By.XPATH, ".//li//span[@aria-label]")

                # Save items of the current category
                category_items = [
                    item.text.strip() for item in items if item.text.strip()
                ]

                # If there are items for a category, add them to the list
                if category_items:
                    about_info.append(f"{category_name}: {category_items}")
            
            if not about_info:
                about_info = None
                
            return about_info

        except (TimeoutException, NoSuchElementException):
            print("Failed to load 'About' section.")
            return []
    
    def close(self):
        """Close the Selenium driver."""
        self.driver.quit()