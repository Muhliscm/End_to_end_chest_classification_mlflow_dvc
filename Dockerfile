FROM python:3.8-alpine
RUN apt update -y && apt install awscli -y
COPY . /app
WORKDIR /app
RUN pip install requirments.txt
CMD [ "python","app.py" ]