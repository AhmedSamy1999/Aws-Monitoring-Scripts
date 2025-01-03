# AWS Monitoring Scripts
A Python-based project for monitoring and managing AWS resources like EC2 instances and S3 buckets.

## Description
This project provides a simple interface to monitor and manage AWS resources using Python and boto3. 

- Creating new EC2 instances 
- Creating new S3 buckets
- Listing EC2 instances and their states
- Listing S3 buckets


## Prerequisites
- Python 3.8 or higher
- AWS account with appropriate IAM permissions
- AWS credentials configured in .env

## Installation

1. Clone the repository:
```sh
git clone https://github.com/yourusername/aws-monitoring-scripts.git
cd aws-monitoring-scripts
```

2. Create and activate a virtual environment:
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install requirements:
```sh
pip install -r requirements.txt
```

## Project Structure
```sh
aws-monitoring-scripts/
├── services/
│   ├── __init__.py
│   ├── ec2_manager.py
│   ├── s3_manager.py
│   └── logger.py
├── .env
├── main.py
├── requirements.txt
└── README.md
```


## Configuration
- Environment Variables
Required environment variables in .env:

* AWS_ACCESS_KEY_ID: Your AWS access key
* AWS_SECRET_ACCESS_KEY: Your AWS secret access key
* AWS_DEFAULT_REGION: AWS region (e.g., "eu-west-3")


## AWS Permissions
The AWS user requires the following permissions:
## ![alt text](image.png)

## Error Handling
The project includes comprehensive error handling:

* All AWS operations are wrapped in try-except blocks
* Errors are logged with detailed messages
* Main script captures and logs any unhandled exceptions


## Logging
The project uses a configured logger that:
* Outputs to console
* Includes timestamps
* Shows log level and component name

