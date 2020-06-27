## Requirements

* Serverless Framework
* Docker

## Deployment

Run the following command in the root directory to deploy.

`sls deploy -v --stage <stage_name>`

_Note: Replace the stage variable to your stage name._

## Docker image

The service runs on AWS Fargate and requires the service to be available as a Docker image.

#### Building the docker image

This repo has a Dockerfile in the root folder, which builds the image.

Use the following commands to build the image and push to the vfan docker hub repo.

```
docker build  -t <Docker_Repo>/<Image_Name> .
docker push <Docker_Repo>/<Image_Name> 
```

Next, update the docker [image name](https://github.com/murali44/fargate-scaling/blob/master/resources/Fargate/task.yml#L4) in the Fargate resource file.

## Architecture

See [here](https://www.blog.muraliallada.com/fargate-scaling/) for design details.