import os
import time
import logging
from src.main.config.WebDriverConfig import WebDriverConfig
from selenium.webdriver.common.by import By
from src.main.mail.Mail import Mail

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger()

class ExampleRuns:

    @staticmethod
    def go_to_website():
        driver, download_folder = WebDriverConfig().get_driver_and_download_folder()
        #Go to example.com and show text output
        driver.get("https://example.com/")
        logger.info(driver.find_element(By.TAG_NAME, "h1").text)
        
        time.sleep(5)
        driver.quit()

    @staticmethod
    def take_screenshot_from_website():
        driver, download_folder = WebDriverConfig().get_driver_and_download_folder()

        #Go to example.com and show text output
        driver.get("https://example.com/")
        logger.info(driver.find_element(By.TAG_NAME, "h1").text)

        #Take screenshot
        saved_screenshot_filename = os.path.join(download_folder, "screenshot1.png")
        print(saved_screenshot_filename)
        driver.save_screenshot(saved_screenshot_filename)

        #Show files in download folder
        download_folder_files_list = os.listdir(download_folder)
        logger.info(f"Files in download dir {download_folder_files_list}")

        time.sleep(5)
        driver.quit()

    @staticmethod
    def download_file_from_website():
        driver, download_folder = WebDriverConfig().get_driver_and_download_folder()

        #Go to kailynw.com
        driver.get("http://kailynw.com")
        time.sleep(5)

        #Take screenshot
        saved_screenshot_filename = os.path.join(download_folder, "screenshot1.png")
        print(f"Screenshot file path: {saved_screenshot_filename}")
        driver.save_screenshot(saved_screenshot_filename)

        #Download resume
        logger.info("Attempting to download file...")
        download_resume_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/a")
        download_resume_button.click()
        time.sleep(5)

        #Show files that have been downloaded or placed in download folder
        download_folder_files_list = os.listdir(download_folder)
        logger.info(f"Files in download dir {download_folder_files_list}")

        # Mail().send_mail(saved_screenshot_filename) #For Debugging purposes
        driver.quit()




