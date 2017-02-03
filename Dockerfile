FROM python

WORKDIR /src

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD src/ .

CMD ["python", "ecs_ondemand.py"]