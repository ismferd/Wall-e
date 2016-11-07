import logging

from clean_cloudformation import CleanerCloudFormation
from clean_ec2_instances import CleanerEc2Instances
from clean_launchconfiguration import CleanerLaunchConfiguration
from clean_snapshots import CleanerSnapshots
from get_sts import StsInfo

logger = logging.getLogger('Wall-e')


class WalleConfiguration(object):
    def __init__(self, connection):
        self.connection = connection

    def clean_cloudformation(self, resource, account_name, dust_file):
        cformation = CleanerCloudFormation(self.connection.get_resource_connection_to_aws(resource, account_name))
        plants_to_save = self.save_plants(dust_file)
        cloudformations_dust = []
        for line in plants_to_save:
            cloudformations_dust.append(line)
            logger.info("Saving {0} plant".format(line))
        cformation.cleaner_stacks(cloudformations_dust)

    def clean_launchconfiguration(self, resource, account_name):
        launch_config = CleanerLaunchConfiguration(self.connection.get_client_connection_to_aws(resource, account_name))
        launch_config.cleaner_launch_config()

    def clean_ec2_instances(self, resource, account_name, tag):
        ec2 = CleanerEc2Instances(self.connection.get_resource_connection_to_aws(resource, account_name))
        ec2.cleaner_ec2_instances_by_tag(tag)

    def clean_snapshots(self, resource, account_name, days):
        snapshots = CleanerSnapshots(self.connection.get_client_connection_to_aws(resource, account_name))
        snapshots.cleaner_snapshots_older_than(days)

    def get_sts_info(self, resource, account_name):
        sts_info = StsInfo(self.connection.get_client_connection_to_aws(resource, account_name))
        sts_info.get_sts_info()

    def save_plants(self, dust_file):
        return open(dust_file).read().splitlines()



