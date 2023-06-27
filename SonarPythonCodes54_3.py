#This block_public_access allows public ACL to be set:

bucket = s3.Bucket(self,
    "bucket",
    block_public_access=s3.BlockPublicAccess(
        block_public_acls=False,       # Sensitive
        ignore_public_acls=True,
        block_public_policy=True,
        restrict_public_buckets=True
    )
)