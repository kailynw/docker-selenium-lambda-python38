
FROM public.ecr.aws/lambda/python:3.8

RUN yum install -y unzip && \
    yum install -y https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm &&\
    curl -SL https://chromedriver.storage.googleapis.com/2.43/chromedriver_linux64.zip > /tmp/chromedriver.zip && \
    curl -SL https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-55/stable-headless-chromium-amazonlinux-2017-03.zip > /tmp/headless-chromium.zip && \
    unzip /tmp/chromedriver.zip -d /opt/ && \
    unzip /tmp/headless-chromium.zip -d /opt/ && \
    rm /tmp/chromedriver.zip /tmp/headless-chromium.zip

COPY ./requirements.txt /pip-requirements/
RUN pip install -r /pip-requirements/requirements.txt
COPY ./src ${LAMBDA_TASK_ROOT}/src
RUN cd ${LAMBDA_TASK_ROOT}/src && ls -a
CMD [ "src.main.runner.handler" ]
