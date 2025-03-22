# scraper.py

from time import sleep
from selenium.webdriver.common.by import By
from selenium_launcher import SeleniumDriver

class GoogleMapsScraper:
    def __init__(self):
        """Initialize the scraper with a list of URLs and set up the Selenium driver."""
        # self.urls_list = urls_list
        self.selenium_driver = SeleniumDriver()
        self.driver = self.selenium_driver.get_driver()

    def scrape_link(self, url):
        """Scrape a single link and return the name and URL."""
        print("Scraping link:", url)
        self.driver.get(url)
        sleep(1)
        while True:
            try:
                links_list = self.driver.find_elements(By.XPATH, "//a[@class='hfpxzc']")
                self.driver.execute_script("return arguments[0].scrollIntoView();", links_list[-1])
                print('Scrolled')
                if "You've reached the end of the list" in self.driver.page_source:
                    break
                sleep(3)
            except IndexError:
                break
        
        links_list = self.driver.find_elements(By.XPATH, "//a[@class='hfpxzc']")

        company = {}

        for link_element in links_list:
            link = link_element.get_attribute("href")
            name = link_element.get_attribute("aria-label")

            company[name] = link

        return company

    def close(self):
        """Close the Selenium driver."""
        self.selenium_driver.quit()
