import sys
import logging
import chromedriver_autoinstaller as chrome_installer
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger()

class WebDriverConfig():
        
    def get_driver(self):
        is_local = self._is_local()

        if is_local:
            logger.info("Retrieving Local Chrome Driver...")
            return self._get_local_driver()
        else:
            logger.info("Retrieving AWS Lambda Chrome Driver...")
            return self._get_aws_lambda_driver()
    
    def _get_aws_lambda_driver(self):
        chrome_options = Options()
        chrome_options.binary_location = "/opt/headless-chromium"
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1280x1696")
        chrome_options.add_argument("--single-process")
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome("/opt/chromedriver", chrome_options=chrome_options)
        return driver

    def _get_local_driver(self):
        chrome_installer.install()
        chrome_options= Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--window-size=1280x1696")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        return driver

    def _is_local(self):
        available_local_os = ["darwin", "win32"] #darwin = MACOS | win32 = Windows
        os = sys.platform
        logger.info(f"Current Operating System: {os}")
        if os in available_local_os:
            return True
        else:
            return False

    
