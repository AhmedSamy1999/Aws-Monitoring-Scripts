from services.ec2_manager import EC2Manager
from services.s3_manager import S3Manager
from utils.logger import setup_logger

def main():
    logger = setup_logger()
    
    try:
        # Initialize service managers
        ec2 = EC2Manager()
        s3 = S3Manager()
        
        # Example operations
        print("\nEC2 Instances:")
        instances = ec2.list_instances()
        for instance in instances:
            print(f"- {instance['InstanceId']}: {instance['State']['Name']}")
            
        print("\nS3 Buckets:")
        buckets = s3.list_buckets()
        for bucket in buckets:
            print(f"- {bucket['Name']}")
            
    except Exception as e:
        logger.error(f"Error in main: {str(e)}")

if __name__ == "__main__":
    main()