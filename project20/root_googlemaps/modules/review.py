import time
from selenium_launcher import SeleniumDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


class ReviewCollector:
    def __init__(self, driver, max_reviews=30, max_time_limit=60):
        """Initialize ReviewCollector with a Selenium driver, max review count, and max time limit."""
        self.driver = driver
        self.max_reviews = max_reviews
        self.max_time_limit = max_time_limit
        
    def collect_reviews(self):
        print('Start scraping reviews')
        """Collect reviews up to a specified maximum count or timeout."""
        reviews_list = []
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(@aria-label, 'Reviews')]")
                )
            ).click()
            
            reviews_container = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//div[contains(@class, 'm6QErb DxyBCb kA9KIf dS8AEf XiKgde')]",
                    )
                )
            )

            unique_reviews = set()
            start_time = time.time()

            while len(unique_reviews) < self.max_reviews:
                if time.time() - start_time > self.max_time_limit:
                    print("Time limit exceeded, stopping review collection.")
                    break
                try:
                    self.driver.execute_script(
                        "arguments[0].scrollTop = arguments[0].scrollHeight",
                        reviews_container,
                    )
                except StaleElementReferenceException:
                    print("Failed to scroll the reviews container.")
                    break
                
                reviews_elements = self.driver.find_elements(
                    By.XPATH, "//div[@data-review-id]"
                )

                for review in reviews_elements:
                    review_id = review.get_attribute("data-review-id")
                    if review_id not in unique_reviews:
                        unique_reviews.add(review_id)
                        author_name = review.get_attribute("aria-label").strip()
                        review_text = review.find_elements(
                            By.XPATH, ".//span[@class='wiI7pd']"
                        )
                        review_text = (
                            review_text[0].text.strip() if review_text else None
                        )
                        reviews_list.append(
                            {"Author": author_name, "Review": review_text}
                        )
                        if len(unique_reviews) >= self.max_reviews:
                            break
        except TimeoutException:
            print("Failed to download or collect feedback.")
        
        if not reviews_list:
            reviews_list = None
        
        print('Reviews done')
        return reviews_list
    
    def close(self):
        """Close the Selenium driver."""
        self.driver.quit()
