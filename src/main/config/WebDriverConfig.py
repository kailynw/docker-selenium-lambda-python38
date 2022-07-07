import os
import sys
import logging
import chromedriver_autoinstaller as chrome_installer
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger()

class WebDriverConfig():
        
    def get_driver_and_download_folder(self):
        is_local = self._is_local()

        if is_local:
            logger.info("Retrieving Local Chrome Driver...")
            return self._get_local_driver_and_download_folder()
        else:
            logger.info("Retrieving AWS Lambda Chrome Driver...")
            return self._get_aws_lambda_driver_and_download_folder()
    
    def _get_aws_lambda_driver_and_download_folder(self):
        chrome_options = Options()

        download_folder = self._get_lambda_download_path()
        prefs = {
            "download.default_directory": download_folder,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True
        }
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.binary_location = "/opt/chrome-linux/chrome"
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1280x1696")
        chrome_options.add_argument("--single-process")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36")

        driver = webdriver.Chrome("/opt/chromedriver", chrome_options=chrome_options)
        return (driver, download_folder)

    def _get_local_driver_and_download_folder(self):
        chrome_installer.install()
        chrome_options= Options()

        download_folder = self._get_local_download_path()
        prefs = {
            "download.default_directory": download_folder,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True
        }

        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--window-size=1280x1696")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        return (driver, download_folder)

    def _is_local(self):
        available_local_os = ["darwin", "win32"] #darwin = MACOS | win32 = Windows
        os = sys.platform
        logger.info(f"Current Operating System: {os}")
        if os in available_local_os:
            return True
        else:
            return False

    def _get_local_download_path(self):
        project_folder = "/Users/kailynwilliams/Desktop/AllDesktopFIles/Python-Selenium-3.8-POC/docker-selenium-lambda-python38"            
        download_path = os.path.join(project_folder, "selenium_download_folder")
        print(f"Local download folder: {download_path}")

        #Create download path if it doesnt exist
        if not os.path.isdir(download_path):
            os.mkdir(download_path)

        return download_path
    
    def _get_lambda_download_path(self):
        tmp_folder = "/tmp"
        download_path = os.path.join(tmp_folder, "selenium_download_folder")
        print(f"Lambda download folder: {download_path}")

        #Create download path if it doesnt exist
        if not os.path.isdir(download_path):
            os.mkdir(download_path)

        return download_path



    
