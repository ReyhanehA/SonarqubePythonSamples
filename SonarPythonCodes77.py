bucket = s3.Bucket(self,"bucket",
    encryption=s3.BucketEncryption.UNENCRYPTED       # Sensitive
)