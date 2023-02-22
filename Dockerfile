FROM python:3.9


RUN mkdir /test_task
WORKDIR /test_task

COPY requirements.txt /test_task/
RUN pip install -r requirements.txt

COPY . /test_task/
CMD [ "python", "manage.py", "runserver", "0.0.0.0:80"]
EXPOSE 80
