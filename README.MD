
## Deployment

In the root directory, use the following command to deploy.

`sls deploy -v --stage <stage_name>`

_Note: Replace the stage variable to your name._  All deployed AWS resources are prefixed with the stage name to help identify resources belonging to a particular stage or developer.

By default all stages except 'prod' are deployed to us-west-2 (Oregon). Only 'prod' gets deployed to us-east-2 (Ohio).

## Docker image

The service runs on AWS Fargate and requires the service to be available as a Docker image.

#### Building the docker image

This repo has a Dockerfile in the root folder, which builds the image.

Use the following commands to build the image and push to the vfan docker hub repo.

```
docker build  -t <Docker_Repo>/<Image_Name> .
docker push <Docker_Repo>/<Image_Name> 
```

Next, update the docker [image name]() in the Fargate resource file.

## Architecture

See [here](https://www.blog.muraliallada.com/fargate-scaling/) for design details.