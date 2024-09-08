import boto3


print("Reading from DynamoDB:")
dynamodb = boto3.resource(
    "dynamodb",
    endpoint_url="http://localhost:8000",
    region_name="us-east-1",
    aws_access_key_id="dummy",
    aws_secret_access_key="dummy",
)
table = dynamodb.Table("MyTable")

response = table.scan()
items = response["Items"]
for item in items:
    print(f"  - {item}")
