"""This module provides the main functionality of HTTPie.
Invocation flow:
  1. Read, validate and process the input (args, `stdin`).
  2. Create and send a request.
  3. Stream, and possibly process and format, the parts
     of the request-response exchange selected by output options.
  4. Simultaneously write to `stdout`
  5. Exit.
"""


import argparse
from boto_connections import BotoConnections
import logging
from wall_e import WalleConfiguration


def main():
    """
    The main function.
    Pre-process args, handle some special types of invocations,
    and run the main program with error handling.
    Return exit status code.
    """
    logger = logging.getLogger('Wall-e')
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--resource', help='AWS Resource', required=True)
    parser.add_argument('-t', '--tag', nargs='+', help='AWS Tag', required=False)
    parser.add_argument('-D', '--days', nargs='+', help='Days old to delete', required=False)
    parser.add_argument('-a', '--aws_account', help='AWS account name', required=True)
    parser.add_argument('-d', '--dust', help='cloudformation whitelist: you must write a file containing the list of '
                                             'cloudformation names that will not be deleted', required=False)

    args = parser.parse_args()
    resource = args.resource
    account_name = args.aws_account
    dust = args.dust
    tag = args.tag
    days = args.days

    logger.info('Building a Wall-e bot...')
    logger.info('Wall-e are going to clean: {0} in account {1}'.format(resource, account_name))
    connection = BotoConnections()
    walle = WalleConfiguration(connection)
    logger.info("Cleaning your ecosystem and saving plants")

    sts_info = walle.get_sts_info('sts', account_name)
    print(sts_info)

    if resource == 'cloudformation':
        walle.clean_cloudformation(resource, account_name, dust)
    if resource == 'autoscaling':
        walle.clean_launchconfiguration(resource, account_name)
    if resource == 'ec2':
        walle.clean_ec2_instances(resource, account_name, tag)
    if resource == 'snapshots':
        walle.clean_snapshots('ec2', account_name, days)


    logger.info("Finished, your {0} are clean".format(resource))

if __name__ == '__main__':
    main()

