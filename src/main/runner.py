import sys
import time
import logging
from selenium.webdriver.common.by import By
from src.main.config.WebDriverConfig import WebDriverConfig

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger()

def handler(event=None, context=None):
    logger.info(f"Python Version info: {sys.version}")
    logger.info(f"Event: {event}")

    #Initiate Driver
    driver = WebDriverConfig().get_driver()

    #Go to example.com and show text output
    driver.get("https://example.com/")
    logger.info(driver.find_element(By.TAG_NAME, "h1").text)
    time.sleep(5)
    driver.quit()

    return "This actually works lol"

if __name__ == '__main__':
    handler(None, None)

