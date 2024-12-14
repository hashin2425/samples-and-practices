import boto3

if __name__ == "__main__":
    s3 = boto3.resource(
        "s3",
        endpoint_url="http://localhost:9000",
        aws_access_key_id="admin",
        aws_secret_access_key="adminPass123",
    )

    # MinIOのバケット出力
    for bucket in s3.buckets.all():
        print(bucket.name)
    print("")

    # MinIO内の`sample-data-123.txt`の中身出力
    obj = s3.Object("sample-bucket-123", "sample-data-123.txt")
    res = obj.get()
    print(res["Body"].read().decode())
