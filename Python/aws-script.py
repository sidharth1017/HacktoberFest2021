#boto script that alert about disk size and increase disk size 1 gb
import boto3, sys

# This script requires an AWS profile name to be passed to it
if len(sys.argv) < 2:
    print("A profile parameter is required.")
    profile = input("Enter a profile name: ")
    boto3.setup_default_session(profile_name=profile)
else:
    profile = (sys.argv[1])
    boto3.setup_default_session(profile_name=sys.argv[1])

# Create EC2 resource
ec2 = boto3.resource('ec2')

# Getting all running instances
instances = ec2.instances.all()

# Create CloudWatch client
cloudwatch = boto3.client('cloudwatch')

for i in instances:
    i_name = "unnamed"
    for tag in i.tags:
        if tag['Key'] == "Name":
            i_name = tag['Value']
    print(i_name, i.id)

    # Create alarm
    cloudwatch.put_metric_alarm(
        AlarmName = i_name + "-(" + i.id + ")-" + "Disk-Utilization-85-Pct",
        ComparisonOperator = 'LessThanOrEqualToThreshold',
        EvaluationPeriods = 10,
        MetricName = 'LogicalDisk % Free Space',
        Namespace = 'CWAgent',
        Period = 60,
        Statistic = 'Average',
        Threshold = 15.0,
        ActionsEnabled = False,
        AlarmDescription = 'Alarm when there is 15% disk space or less',
        Dimensions = [
            {
                'Name': 'InstanceId',
                'Value': id,
                'Name': 'instance',
                'Value': '_Total'
            },
        ],
        Unit = 'Seconds',
        TreatMissingData = 'notBreaching'
    )
