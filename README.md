CLOUD COST OPTIMIZATION – AUTOMATED EBS SNAPSHOT CLEANUP
1. This code is meant to be used as an AWS Lambda function.
2. Here's the process to test the code:
   1.Create an EC2 Instance, and by default a Volume will be attached to the instance
   2. Create a Snapshot and associate it to that Volume
   3. Copy and paste this Python script into a Lambda function
   4. Deploy the code
   5. Create a test trigger (can also use CloudWatch to trigger automatically)
   6. Add the following permissions to the EC2 service role (either in one policy or multiple policies)
     1. DescribeSnapshots
     2. DescribeInstances
     3. DescribeVolumes
     4. DeleteSnapshots
   7. Manually delete the EC2 instance, and the associated Volume will be deleted as well
   8. Now trigger the test, and you'll see the Snapshot will also be deleted, since it's not associated with a volume. 
   
   
