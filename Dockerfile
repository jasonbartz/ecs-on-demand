FROM python

WORKDIR /src

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD ecs_on_demand/ .

CMD ["python", "runner.py"]