import boto3

# write a function that list all the buckets in my account
def list_buckets():
    s3 = boto3.resource("s3")
    for bucket in s3.buckets.all():
        print(bucket.name)


# invoke the function
list_buckets()
