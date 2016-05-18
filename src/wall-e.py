#!/usr/bin/python

from clean_cloudformation import CleanerCloudFormation
from boto_connections import BotoConnections
import sys


args = str(sys.argv)
profile = str(sys.argv[1])

connection_cloudformation = BotoConnections().get_resource_connection_to_aws("cloudformation", profile)
cformation = CleanerCloudFormation(connection_cloudformation)

cloudformation_dust_file = open("dust/cloudformation_dust").read().splitlines()

cloudformations_dust = []
for line in cloudformation_dust_file:
    cloudformations_dust.append(line)

cformation.cleaner_stacks(cloudformations_dust)