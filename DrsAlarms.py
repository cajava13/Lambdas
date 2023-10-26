import boto3

class CreateAlarm:
    def __init__(self):
        # Create CloudWatch client
        self.cloudwatch_client = boto3.client('cloudwatch')

    def create_alarm(self):
        try:
            response = self.cloudwatch_client.put_metric_alarm(
                AlarmName = 'LagDuration',
                AlarmDescription='the age of the latest consistent snapshot, in seconds',
                ActionsEnabled=True,
                MetricName='LagDuration',
                Namespace='AWS/DRS',
                Statistic='Average',
                Period=300,
                EvaluationPeriods=5,
                Threshold=1,
                ComparisonOperator='GreaterThanOrEqualToThreshold',
                Unit='Seconds'
            )
            return {
                'statusCode': 200,
                'body': 'Alarm created successfully!'
            }
        except Exception as e:
            print(f'Error creating Alarm')
            return {
                'statusCode': 500,
                'body': 'Error creating Alarm'
            }

def lambda_handler(event, context):
    return CreateAlarm().create_alarm()