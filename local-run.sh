#!/bin/bash -e

IMG=ecs-on-demand

docker build -t ${IMG} .
docker run -e AWS_REGION=`cat ~/.envs/sandbox/AWS_REGION` -e AWS_ACCESS_KEY_ID=`cat ~/.envs/sandbox/AWS_ACCESS_KEY_ID` -e AWS_SECRET_ACCESS_KEY=`cat ~/.envs/sandbox/AWS_SECRET_ACCESS_KEY` ${IMG} python runner.py $1 $2