FROM python:3.8.2-slim
COPY requirements.txt /
RUN pip3 install -r requirements.txt
COPY /src /src
ENTRYPOINT [ "python", "/src/fargate_task.py" ]