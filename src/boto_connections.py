import boto3


class BotoConnections(object):
    def get_resource_connection_to_aws(self, resource, aws_account_name):
        connection = boto3.session.Session(region_name="eu-west-1", profile_name=aws_account_name)
        connection_resource = connection.resource(resource, region_name="eu-west-1")
        return connection_resource

    def get_client_connection_to_aws(self, resource, aws_account_name):
        connection = boto3.session.Session(region_name="eu-west-1", profile_name=aws_account_name)
        connection_client = connection.client(resource, region_name="eu-west-1")
        return connection_client