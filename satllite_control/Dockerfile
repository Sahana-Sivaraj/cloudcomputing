# Dockerfile
FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1
COPY requirements.txt /frontendapp/requirements.txt
WORKDIR /frontendapp
RUN pip install -r requirements.txt
COPY . /frontendapp
ENTRYPOINT ["python"]
CMD ["run.py"]