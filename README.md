CLOUD COST OPTIMIZATION – AUTOMATED EBS SNAPSHOT CLEANUP
1. This code is meant to be used as an AWS Lambda function.
2. Here's the process to test the code:
   Create an EC2 Instance, and by default a Volume will be attached to the instance
   Create a Snapshot and associate it to that Volume
   Copy and paste this Python script into a Lambda function
   Deploy the code
   Create a test trigger (can also use CloudWatch to trigger automatically)
   Add the following permissions to the EC2 service role (either in one policy or multiple policies)
     DescribeSnapshots
     DescribeInstances
     DescribeVolumes
     DeleteSnapshots
   Manually delete the EC2 instance, and the associated Volume will be deleted as well
   Now trigger the test, and you'll see the Snapshot will also be deleted, since it's not associated with a volume. 
   
   
