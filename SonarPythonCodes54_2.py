#The attribute BLOCK_ACLS only blocks and ignores public ACLs:

bucket = s3.Bucket(self,
    "bucket",
    block_public_access=s3.BlockPublicAccess.BLOCK_ACLS     # Sensitive
)