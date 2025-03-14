import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    #Get all EBS Snapshots
    response = ec2.describe_snapshots(
        OwnerIds=['self']
    )

    #Get all active EC2 instance IDs
    instances_response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': [
                    'running'
                ]
            }
        ]
    )
    active_instance_ids = set()

    for reservation in instances_response['Reservations']:
        for instance in reservation['Instances']:
            active_instance_ids.add(instance['InstanceId'])

    #iterate through each snapshot and delete if it's not attached to any volume or the volume is not active
    for snapshot in response['Snapshots']:
        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot.get('VolumeId')
        if not volume_id:
            # Delete the snapshot if it's not attached to any volume
            ec2.delete_snapshot(SnapshotId=snapshot_id)
            print(f"Deleted snapshot {snapshot_id} because it was not attached to any volume")
        else:
            # Check if the volume still exists
            try:
                volume_response = ec2.describe_volumes(VolumeIds=[volume_id])
                if not volume_response['Volumes'][0]['Attachments']:
                    # Delete the snapshot if the volume is not attached to any instance
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted snapshot {snapshot_id} because the volume {volume_id} is not attached to any instance")
            except ec2.exceptions.ClientError as e:
                if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                    # The volume Associated with the snapshot no longer exists
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted snapshot {snapshot_id} because the volume {volume_id} no longer exists")