#!/usr/bin/python
import argparse
from clean_cloudformation import CleanerCloudFormation
from boto_connections import BotoConnections
import logging


class WalleConfiguration(object):
    def __init__(self, dust_file, connection):
        self.connection = connection
        self.cformation = CleanerCloudFormation(self.connection)
        self.cloudformation_dust_file = dust_file

    def clean_cloudformation(self):
        plants_to_save = self.save_plants()
        cloudformations_dust = []
        for line in plants_to_save:
            cloudformations_dust.append(line)
            print (line)
        self.cformation.cleaner_stacks(cloudformations_dust)

    def save_plants(self):
        return open(self.cloudformation_dust_file).read().splitlines()

if __name__ == '__main__':
    LOG_FILENAME = "logs/wall-e.log"
    logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--resource', help='AWS Resource', required=True)
    parser.add_argument('-a', '--aws_account', help='AWS account name', required=True)
    parser.add_argument('-d', '--dust', help='Dust file location', required=True)
    args = parser.parse_args()
    resource = args.resource
    account_name = args.aws_account
    connection = BotoConnections().get_resource_connection_to_aws(resource, account_name)
    dust = args.dust
    walle = WalleConfiguration(dust, connection)
    walle.clean_cloudformation()
