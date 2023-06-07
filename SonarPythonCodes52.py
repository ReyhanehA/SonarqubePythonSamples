bucket = s3.Bucket(self, "bucket",
    access_control=s3.BucketAccessControl.PUBLIC_READ_WRITE     # Sensitive
)

s3deploy.BucketDeployment(self, "DeployWebsite",
    access_control=s3.BucketAccessControl.PUBLIC_READ_WRITE     # Sensitive
)