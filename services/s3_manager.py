import boto3
from utils.logger import get_logger

class S3Manager:
    def __init__(self):
        self.s3 = boto3.client('s3')
        self.logger = get_logger()
    
    def list_buckets(self):
        """List all S3 buckets"""
        try:
            response = self.s3.list_buckets()
            return response['Buckets']
        except Exception as e:
            self.logger.error(f"Error listing S3 buckets: {str(e)}")
            raise
    
    def create_bucket(self, bucket_name, region='us-east-1'):
        """Create a new S3 bucket"""
        try:
            self.s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
            return True
        except Exception as e:
            self.logger.error(f"Error creating S3 bucket: {str(e)}")
            raise