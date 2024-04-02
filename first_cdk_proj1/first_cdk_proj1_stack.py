from aws_cdk import (
    # Duration,
    aws_s3 as _s3,
    Duration,
    Stack
    # aws_sqs as sqs,
)
from constructs import Construct

class FirstCdkProj1Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        _s3.Bucket(
            self,
            "myBucketId",
            bucket_name="bucketcitomio1289371298p",
            encryption=_s3.BucketEncryption.S3_MANAGED,
            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL,
            versioned=True,
            object_lock_default_retention=_s3.ObjectLockRetention.governance(Duration.days(10))
        )
