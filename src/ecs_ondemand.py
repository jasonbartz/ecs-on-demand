import os
import sys
import boto3

desc = {

	"image": "",
	"data": "",
	"role": "",
	"cluster": ""
}

def _get_name_from_image(image):
	print(image)
	return image.replace("/", "_")

def run(event):

	event_name = _get_name_from_image(event["image"])

	task_def = {
			"family": event_name,
			"containerDefinitions": [
				{
					"name": "runner",
					"image": event["image"],
					"memoryReservation": 512,
					"essential": True,
					# "privileged": true,
					# "logConfiguration": {
					# 	"logDriver": "awslogs",
					# 	"options": {
					# 		"awslogs-group": "/nile-pipeline",
					# 		"awslogs-region": "us-east-1",
					# 		"awslogs-stream-prefix": "test"
					# 	}
					# }
				}
			]
		}


	if event.get("task"):
		task_def["taskRoleArn"] = "arn:aws:iam::210767430655:role/Nile"

	ecs = boto3.client("ecs", region_name=os.environ.get("AWS_REGION"))
	ecs.register_task_definition(**task_def)


	fire_task = ecs.run_task(**{

				"cluster": event["cluster"],
				"taskDefinition": event_name,
				"overrides": {
					"containerOverrides": [
						{
							"name": "runner",
							"environment": [
								{
									"name": "DATA",
									"value": event.get("data", "")
								}
							]
						}
					]
				},
				"count": 1,
				"startedBy": "ecs on demand"
			}
	)
	print(fire_task)

if __name__ == "__main__":

	event = {}
	try:
		event = {
				"image": sys.argv[1],
				"cluster": sys.argv[2],
				# "data": ,
				# "role": "",
		}
	except:
		print("Usage: python ecs_ondemand.py <image> <cluster> [data] [role]")
		sys.exit(1)

	run(event)
