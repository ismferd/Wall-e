#!/usr/bin/python

from clean_cloudformation import CleanerCloudFormation
from boto_connections import BotoConnections
import sys
import logging

LOG_FILENAME = "logs/wall-e.log"
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)


class WalleConfiguration(object):
    def __init__(self, resource, profile):
        self.connection = BotoConnections().get_resource_connection_to_aws(resource, profile)
        self.cformation = CleanerCloudFormation(self.connection)
        self.cloudformation_dust_file = open("dust/cloudformation_dust").read().splitlines()

    def clean_cloudformation(self):
        cloudformations_dust = []
        for line in self.cloudformation_dust_file:
            cloudformations_dust.append(line)
        self.cformation.cleaner_stacks(cloudformations_dust)

if __name__ == '__main__':
    args = str(sys.argv)
    profile = str(sys.argv[1])
    resource = str(sys.argv[2])
    walle = WalleConfiguration(resource, profile)
    walle.clean_cloudformation()
