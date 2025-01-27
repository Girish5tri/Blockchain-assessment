import boto3
import requests
import time

class BlockchainNode:

    def __init__(self, aws_access_key, aws_secret_key):
        # Initialize AWS EC2 client with credentials
        self.ec2 = boto3.client('ec2',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name='us-east-1'
        )
        self.instance_id = None
        self.public_ip = None

    def deploy(self):
        # Deploy an EC2 instance with Ethereum node
        instance = self.ec2.run_instances(
            ImageId='ami-0261755bbcb8c4a84',  
            InstanceType='t2.micro',
            MinCount=1,
            MaxCount=1,
            UserData='''#!/bin/bash
                apt-get update
                apt-get install -y ethereum
                geth --syncmode "light" --http
            '''
        )
        
        self.instance_id = instance['Instances'][0]['InstanceId']
        print(f"Deployed node with ID: {self.instance_id}")
        
        # Get the public IP of the deployed instance
        instance_info = self.ec2.describe_instances(InstanceIds=[self.instance_id])
        self.public_ip = instance_info['Reservations'][0]['Instances'][0]['PublicIpAddress']
        print(f"Node IP: {self.public_ip}")

    def monitor(self):
        # Continuously monitor the node's health
        while True:
            try:
                # Check if node is respondig to HTTP requests
                response = requests.get(f'http://{self.public_ip}:8545')
                if response.status_code != 200:
                    print(" Warning: Node is not responding!")
                else:
                    print(" Node is running")
            except:
                print("Node is down!")

            # Checks every 5 minutes
            time.sleep(300)  
            
# Example usage
if __name__ == "__main__":
    # Create a new blockchain node instance
    node = BlockchainNode(
        aws_access_key='YOUR_ACCESS_KEY',
        aws_secret_key='YOUR_SECRET_KEY'
    )
    
    # Deploy and start monitoring
    node.deploy()
    node.monitor()