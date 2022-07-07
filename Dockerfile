
FROM public.ecr.aws/lambda/python:3.8

# I am downloading...
# Google Chrome Stable (resolve chrome dependency issues)
# Chrome Driver Version 89.0.4389.23
# Chromium Browser Version 89.0.4389.47 (specified in url: 843831)

RUN yum install -y unzip && \
    yum install -y https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm &&\
    curl -SL https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_linux64.zip > /tmp/chrome-driver.zip && \
    curl -SL https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Linux_x64%2F843831%2Fchrome-linux.zip?alt=media > /tmp/chrome-linux.zip && \
    unzip /tmp/chrome-driver.zip -d /opt/ && \
    unzip /tmp/chrome-linux.zip -d /opt/ && \
    rm /tmp/chrome-driver.zip /tmp/chrome-linux.zip

COPY ./requirements.txt /pip-requirements/
RUN pip install -r /pip-requirements/requirements.txt
COPY ./src ${LAMBDA_TASK_ROOT}/src
CMD [ "src.main.runner.handler" ]
