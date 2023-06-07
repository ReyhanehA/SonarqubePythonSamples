By default, when not set, the block_public_access is fully deactivated (nothing is blocked):

bucket = s3.Bucket(self,
    "bucket"        # Sensitive
)
----------------------------------------------------
This block_public_access allows public ACL to be set:

bucket = s3.Bucket(self,
    "bucket",
    block_public_access=s3.BlockPublicAccess(
        block_public_acls=False,       # Sensitive
        ignore_public_acls=True,
        block_public_policy=True,
        restrict_public_buckets=True
    )
)
----------------------------------------------------
The attribute BLOCK_ACLS only blocks and ignores public ACLs:

bucket = s3.Bucket(self,
    "bucket",
    block_public_access=s3.BlockPublicAccess.BLOCK_ACLS     # Sensitive
)
