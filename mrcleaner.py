#!/usr/bin/python

from delete_cloudformation import DeleteCloudFormation
import sys
from boto import cloudformation

args = str(sys.argv)

profile = str(sys.argv[1])

connection_cloudformation = cloudformation.connect_to_region("eu-west-1", profile_name=profile)
cformation = DeleteCloudFormation(connection_cloudformation)

instancesShouldPersist = open("./whitelist").read().splitlines()

instancesNotDie = []
for line in instancesShouldPersist:
    instancesNotDie.append(line)

cformation.delete_stacks(instancesNotDie)