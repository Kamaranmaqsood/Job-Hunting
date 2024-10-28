from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver (make sure to replace with the path to your WebDriver)
driver = webdriver.Chrome()


def startScraping():
    try:
        # Open Google
        driver.get("https://platform.tracxn.com/a/s/feed/5facfa0bde5c4755bcdc17de/t/companiescovered/t/all/table?s"
                   "=sort%3Drelevance%7Corder%3DDEFAULT")

        # Wait for results to load
        time.sleep(200)

        # Retrieve the titles of search results
        results = driver.find_elements(By.CSS_SELECTOR, 'h3')
        for idx, result in enumerate(results, start=1):
            print(f"{idx}. {result.text}")

    finally:
        # Close the browser
        driver.quit()
