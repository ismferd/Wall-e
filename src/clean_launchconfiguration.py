import botocore
import logging

logger = logging.getLogger('Wall-e')


class CleanerLaunchConfiguration(object):

    def __init__(self, connection_launch_configuration):
        self.connection_launch_configuration = connection_launch_configuration

    def get_all_launch_configuration(self):
        return self.connection_launch_configuration.describe_launch_configurations()['LaunchConfigurations']

    def cleaner_launch_config(self):
        launch_configuration = self.get_all_launch_configuration()
        for launch in launch_configuration:
            try:
                self.connection_launch_configuration.delete_launch_configuration(
                    LaunchConfigurationName=launch['LaunchConfigurationName'])

            except botocore.exceptions.ClientError as error:
                    if "Cannot delete launch configuration" in error.response['Error']['Message']:
                        print (error.response['Error']['Message'])
                        pass
                    else:
                        print (error.response['Error']['Message'])
                        exit(1)
