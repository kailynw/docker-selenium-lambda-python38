# A simple selenium web bot setup for python3.8 running in AWS Lambda


### Big shouts to umihico and his project https://github.com/umihico/docker-selenium-lambda

### I am specifically referencing [this](https://github.com/umihico/docker-selenium-lambda/releases/tag/v5) release from his project to build my project

<hr>

## Deploying and testing changes to AWS:
<br>

*This is the manual build/deployment process for  Docker Selenium Lambda (python 3.8) . You can view [umicho's project](https://github.com/umihico/docker-selenium-lambda) to deploy the project in a more automated fashion using the serverless framework*

<br>
Upload Image to AWS ECR

1. Go to AWS ECR -> Repositories
2. Create a repository named "docker-selenium-lambda-python38"
3. Go to the repository you just made and click "View push commands"
4. Follow the commands displayed to push your docker image to AWS ECR

Use image in AWS Lambda and test

1. Go to AWS Lambda
2. Click "Create function"
3. Select "Container Image" configuration
4. Add Image URI from the image you uploaded or click "Browse Images" to find your image
5. Finish remaining configuration and click "Create function"
6. Test function!
	
<hr>

## Local Testing 

1. In same directory as Dockerfile run
    ```bash
    docker build -t docker-selenium-lambda-python38 --progress=plain .
    ```

2. Run image in container
    ```bash
    docker run -p 9090:8080 docker-selenium-lambda-python38
    ```

1. To execute lambda script, Run command in separate terminal 
    ```bash 
    curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"payload":"hello world!"}' 
    ```

<hr>

## Additional Resources that helped me build the project

- Creating custom lambda docker images from ECR gallery:
https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-create-1

- Docker ECR lambda python3.8 base image for umhico's project (public.ecr.aws/lambda/python:3.8):
https://gallery.ecr.aws/lambda/python


- How to create an AWS Lambda using AWS ECR Docker container image in Python
 https://medium.com/mlearning-ai/how-to-create-an-aws-lambda-using-aws-ecr-docker-container-image-in-python-76203a2c11e2
