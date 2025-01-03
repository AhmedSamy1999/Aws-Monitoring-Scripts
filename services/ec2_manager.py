import boto3
from services.logger import get_logger
import sys

class EC2Manager:
    def __init__(self):
        self.ec2 = boto3.client('ec2')
        self.logger = get_logger()
        #print(sys.path)
    
    def list_instances(self):
        """List all EC2 instances"""
        try:
            response = self.ec2.describe_instances()
            instances = []
            for reservation in response['Reservations']:
                instances.extend(reservation['Instances'])
            return instances
        except Exception as e:
            self.logger.error(f"Error listing EC2 instances: {str(e)}")
            raise
    
    def create_instance(self, ami_id, instance_type='t2.micro'):
        """Create a new EC2 instance"""
        try:
            response = self.ec2.run_instances(
                ImageId=ami_id,
                InstanceType=instance_type,
                MinCount=1,
                MaxCount=1
            )
            return response['Instances'][0]
        except Exception as e:
            self.logger.error(f"Error creating EC2 instance: {str(e)}")
            raise