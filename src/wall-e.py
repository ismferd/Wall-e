#!/usr/bin/python
import argparse
from clean_cloudformation import CleanerCloudFormation
from boto_connections import BotoConnections
import logging

LOG_FILENAME = "logs/wall-e.log"
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)


class WalleConfiguration(object):
    def __init__(self, resource, account_name):
        self.connection = BotoConnections().get_resource_connection_to_aws(resource, account_name)
        self.cformation = CleanerCloudFormation(self.connection)
        self.cloudformation_dust_file = open("dust/cloudformation_dust").read().splitlines()

    def clean_cloudformation(self):
        cloudformations_dust = []
        for line in self.cloudformation_dust_file:
            cloudformations_dust.append(line)
        self.cformation.cleaner_stacks(cloudformations_dust)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--resource', help='AWS Resource', required=True)
    parser.add_argument('-a', '--aws_account', help='AWS account name', required=True)
    args = parser.parse_args()
    resource = args.resource
    account_name = args.aws_account
    walle = WalleConfiguration(resource, account_name)
    walle.clean_cloudformation()
