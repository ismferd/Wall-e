import logging
import botocore

logger = logging.getLogger('Wall-e')


class CleanerEc2Instances(object):
    def __init__(self, connection_ec2):
        self.connection_ec2 = connection_ec2

    def get_all_ec2_instances_by_tag(self, tag):
        return list(self.connection_ec2.instances.filter(
            Filters=[{'Name': 'tag:Name', 'Values': [tag]}]))

    def cleaner_ec2_instances_by_tag(self, tag):
        for instance in self.get_all_ec2_instances_by_tag(tag):
            try:
                instance.terminate()
                logger.info('throw trash... {0}'.format(instance.id))
            except botocore.exceptions.ClientError as error:
                print (error.response['Error']['Message'])

