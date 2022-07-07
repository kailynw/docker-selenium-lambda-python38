import sys
import logging
from src.main.examples.ExampleRuns import ExampleRuns

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger()

def handler(event=None, context=None):
    logger.info(f"Python Version info: {sys.version}")
    logger.info(f"Event: {event}")

    if(event["process"] == "download-file-run"):
        logger.info('Running Download file from website process...')
        ExampleRuns.download_file_from_website()
    elif(event["process"] == "screenshot-run"):
        logger.info('Running take screenshot website process...')
        ExampleRuns.take_screenshot_from_website()
    else:
        logger.info('Running go to website process...')
        ExampleRuns.go_to_website()

    return "Process completed successfully!"

#Local Testing
if __name__ == '__main__':
    # event = {"process": "download-file-run"} 
    # event = {"process": "screenshot-run"}
    event = {"process": ""}
    handler(event, None)

