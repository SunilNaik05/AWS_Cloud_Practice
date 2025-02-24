import boto3
import json

ec2_client = boto3.client("ec2", region_name="us-east-1")  # Change region if needed

def lambda_handler(event, context):
    # Create EC2 instance
    response = ec2_client.run_instances(
        ImageId="ami-0abcdef1234567890",  # Use a valid AMI ID
        InstanceType="t2.micro",
        MinCount=1,
        MaxCount=1,
        KeyName="your-key-pair",  # Ensure the key pair exists
        SecurityGroupIds=["sg-12345678"],  # Replace with your security group
        SubnetId="subnet-12345678"  # Replace with your subnet ID
    )

    instance_id = response["Instances"][0]["InstanceId"]

    # Add a Name tag to the instance
    ec2_client.create_tags(
        Resources=[instance_id],
        Tags=[{"Key": "Name", "Value": "sugar bodies"}]
    )

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "EC2 instance created and named 'sugar bodies'", "InstanceId": instance_id})
    }
