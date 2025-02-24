import boto3
import json

ec2_client = boto3.client("ec2", region_name="us-east-1")  # Change region if needed

def lambda_handler(event, context):
    # Get all running EC2 instances
    response = ec2_client.describe_instances(
        Filters=[{"Name": "instance-state-name", "Values": ["running"]}]
    )

    instances = []
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instances.append(instance["InstanceId"])

    if instances:
        # Terminate the instances
        ec2_client.terminate_instances(InstanceIds=instances)
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Terminated instances", "InstanceIds": instances})
        }
    else:
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "No running instances found"})
        }
