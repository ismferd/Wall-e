#!/usr/bin/python
import argparse
from clean_cloudformation import CleanerCloudFormation
from clean_launchconfiguration import CleanerLaunchConfiguration
from boto_connections import BotoConnections
import logging


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

if __name__ == '__main__':
    logger = logging.getLogger('Wall-e')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('logs/wall-e.log')
    fh.setLevel(logging.ERROR)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--resource', help='AWS Resource', required=True)
    parser.add_argument('-a', '--aws_account', help='AWS account name', required=True)
    parser.add_argument('-d', '--dust', help='Dust file location', required=False)
    args = parser.parse_args()
    resource = args.resource
    account_name = args.aws_account
    dust = args.dust
    logger.info('Building a Wall-e bot...')
    logger.info('Wall-e are going to clean: {0} in account {1}'.format(resource, account_name))
    connection = BotoConnections()
    walle = WalleConfiguration(connection)
    logger.info("Cleaning your ecosystem and saving plants")
    #walle.clean_launchconfiguration(resource, account_name)
    walle.clean_cloudformation(resource, account_name, dust)
    logger.info("Finished, your {0} are clean".format(resource))

