from src.wall_e import WalleConfiguration
from src.clean_launchconfiguration import CleanerLaunchConfiguration
from src.boto_connections import BotoConnections
import mock


class TestWalleConfiguration(object):
    def test_clean_launch_configuration_cleaner_launch_config_called(self):
        boto = mock.Mock(BotoConnections)
        walle = WalleConfiguration(boto)
        clc = CleanerLaunchConfiguration
        clc.get_all_launch_configuration = mock.Mock()
        clc.cleaner_launch_config = mock.Mock()
        walle.clean_launchconfiguration('resource', 'account')
        assert clc.cleaner_launch_config.called







