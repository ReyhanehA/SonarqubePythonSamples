#By default, when not set, the block_public_access is fully deactivated (nothing is blocked):

bucket = s3.Bucket(self,
    "bucket"        # Sensitive
)
