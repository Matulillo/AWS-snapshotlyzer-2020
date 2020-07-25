import boto3
import click

session = boto3.Session(profile_name='matulillo')
ec2 = session.resource('ec2')

def filter_instances(project):
    instances=[]
    if project:
        tagfilter = [{'Name':'tag:Project','Values':[project]}]
        instances = ec2.instances.filter(Filters=tagfilter)
    else:
        instances = ec2.instances.all()
    return instances

@click.group()
def instances():
    """Commands for instances"""

@instances.command('list')
@click.option('--project',default=None,
    help="Only instances for project (tag Project:<Name>)")

def list_instances(project):
    "List instances"

    instances = filter_instances(project)
    for i in instances:
        tags = {t['Key']:t['Value'] for t in i.tags or [] }
        print(','.join((
            i.id,
            i.instance_type,
            i.state['Name'],
            tags.get('Project','<no project>'))))
    return

@instances.command('stop')
@click.option('--project',default=None,
    help="Only instances for project (tag Project:<Name>)")
def stop_instances(project):
    "Stop instances"

    instances = filter_instances(project)
    for i in instances:
        print("Stopping {0}".format(i.id))
        i.stop()
    return

@instances.command('start')
@click.option('--project',default=None,
    help="Only instances for project (tag Project:<Name>)")
def start_instances(project):
    "Start instances"

    instances = filter_instances(project)
    for i in instances:
        print("Starting {0}".format(i.id))
        i.start()
    return


if __name__ == '__main__':
    instances()
