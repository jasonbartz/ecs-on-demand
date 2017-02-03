#!/bin/bash

IMG=ecs-ondemand

docker build -t ${IMG} .
docker run -e AWS_REGION=`cat ~/.envs/sandbox/AWS_REGION` -e AWS_ACCESS_KEY_ID=`cat ~/.envs/sandbox/AWS_ACCESS_KEY_ID` -e AWS_SECRET_ACCESS_KEY=`cat ~/.envs/sandbox/AWS_SECRET_ACCESS_KEY` ${IMG} python ecs_ondemand.py $1 $2