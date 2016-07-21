#!/usr/bin/python
from clean_cloudformation import CleanerCloudFormation
from clean_launchconfiguration import CleanerLaunchConfiguration


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

    def save_plants(self, dust_file):
        return open(dust_file).read().splitlines()



