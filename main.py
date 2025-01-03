from services.ec2_manager import EC2Manager
from services.s3_manager import S3Manager

def display_ec2_instances(ec2_manager):
  
    print("\nEC2 Instances:")
    try:
        instances = ec2_manager.list_instances()
        for instance in instances:
            print(f"- {instance['InstanceId']}: {instance['State']['Name']}")
    except Exception as e:
        print(f"Failed to list EC2 instances: {str(e)}")

def display_s3_buckets(s3_manager):
    
    print("\nS3 Buckets:")
    try:
        buckets = s3_manager.list_buckets()
        for bucket in buckets:
            print(f"- {bucket['Name']}")
    except Exception as e:
        print(f"Failed to list S3 buckets: {str(e)}")

def main():
    
 ec2 = EC2Manager()
 s3 = S3Manager()

 #ec2.create_instance('ami-09be70e689bddcef5')  #ubntu image
 #s3.create_bucket('my-bucket-samy-1234-512351')


 display_ec2_instances(ec2)
 display_s3_buckets(s3)



if __name__ == "__main__":
    main()