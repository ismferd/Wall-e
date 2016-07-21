from src.clean_launchconfiguration import CleanerLaunchConfiguration
import mock
import botocore


class TestCleanLaunchConfiguration(object):
    @mock.patch('botocore.client.BaseClient._make_api_call')
    def test_get_all_launch_configurations_is_called(self, mock_connection):
        clean_launch_configuration = CleanerLaunchConfiguration(mock_connection)
        clean_launch_configuration.get_all_launch_configuration()
        assert mock_connection.describe_launch_configurations.called



