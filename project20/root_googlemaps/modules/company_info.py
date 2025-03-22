# scraper.py

from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class GoogleMapsScraper:
    def __init__(self, driver):
        """Initialize the scraper with the Selenium driver."""
        self.driver = driver

    def get_name(self):
        """Extract the name of the place."""
        try:
            return self.driver.find_element(By.TAG_NAME, "h1").text.strip()
        except NoSuchElementException:
            return None

    def get_address_components(self):
        """Extract address components from the page."""
        try:
            full_address = self.driver.find_element(By.XPATH, "//button[@data-item-id='address']").get_attribute('aria-label').replace('Address: ', '').strip()
            address_parts = full_address.split(',')
            address = address_parts[0]
            country = address_parts[-1].strip()
            
            state_zip = address_parts[-2].strip()
            # city = address_parts[-3].strip()
            city, state, zip_code = state_zip.split(' ')
            
            return full_address, address, country, city, state, zip_code
        except (NoSuchElementException, IndexError, ValueError):
            return None, None, None, None, None, None  
         
    def get_located_in(self):
        """Extract information about the place's location context."""
        try:
            return self.driver.find_element(By.XPATH, "//div[contains(text(), 'Located in:')]").text.replace('Located in: ', '').strip()
        except NoSuchElementException:
            return None

    def get_phone(self):
        """Extract the phone number of the place."""
        try:
            return self.driver.find_element(By.XPATH, "//button[contains(@data-item-id, 'phone:tel')]").get_attribute('data-item-id').replace('phone:tel:', '').strip()
        except NoSuchElementException:
            return None

    def get_website(self):
        """Extract the website link of the place."""
        try:
            return self.driver.find_element(By.XPATH, "//a[contains(@aria-label, 'Website:')]").get_attribute('href')
        except NoSuchElementException:
            return None

    def get_clinic_type(self):
        """Extract the type of the clinic."""
        try:
            return self.driver.find_element(By.XPATH, "//button[@class='DkEaL ']").text.strip()
        except NoSuchElementException:
            return None

    def get_rating(self):
        """Extract the rating of the place."""
        try:
            return self.driver.find_element(By.XPATH, "//div[@class='fontDisplayLarge']").get_attribute('innerHTML')
        except NoSuchElementException:
            return None

    def get_num_reviews(self):
        """Extract the number of reviews."""
        try:
            return self.driver.find_element(By.XPATH, "//span[contains(@aria-label, 'reviews')]").text.replace('(', '').replace(')', '').strip()
        except NoSuchElementException:
            return None

    def get_open_hours(self):
        """Extract open hours and check if the place is open 24/7."""
        try:
            open_hours = self.driver.find_element(By.XPATH, "//span[@class='ZDu9vd']").text.strip()
            open_24_7 = 'Yes' if open_hours == 'Open 24 hours' else 'No'
            return open_hours, open_24_7
        except NoSuchElementException:
            return None, 'No'

    def get_overview(self):
        print('Start scraping overview')
        overview = {}
        overview['name'] = self.get_name()
        overview['full_address'], overview['address'], overview['country'], overview['city'], overview['state'], overview['zip_code'] = self.get_address_components()
        overview['located_in'] = self.get_located_in()
        overview['phone'] = self.get_phone()
        overview['website'] = self.get_website()
        overview['place_type'] = self.get_clinic_type()
        overview['rating'] = self.get_rating()
        overview['num_reviews'] = self.get_num_reviews()
        overview['open_hours'], overview['open_24_7'] = self.get_open_hours()
        
        print('Overview done')
        return overview

    def close(self):
        """Close the Selenium driver."""
        self.selenium_launcher.quit()