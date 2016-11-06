from src.wall_e import WalleConfiguration
from src.clean_ec2_instances import CleanerEc2Instances
from src.clean_launchconfiguration import CleanerLaunchConfiguration
from src.boto_connections import BotoConnections
from src.clean_cloudformation import CleanerCloudFormation
import mock


class TestWalleConfiguration(object):
    def test_clean_launch_configuration_cleaner_launch_config_called(self):
        boto = mock.Mock(BotoConnections)
        walle = WalleConfiguration(boto)
        lc_cleaner = CleanerLaunchConfiguration
        lc_cleaner.get_all_launch_configuration = mock.Mock()
        lc_cleaner.cleaner_launch_config = mock.Mock()
        walle.clean_launchconfiguration('resource', 'account')
        assert lc_cleaner.cleaner_launch_config.called

    def test_clean_ec2_instances_cleaner_ec2_instances_by_tag_called(self):
        boto = mock.Mock(BotoConnections)
        walle = WalleConfiguration(boto)
        ec2_instances = CleanerEc2Instances
        ec2_instances.save_ec2_instances_by_tag = mock.Mock()
        ec2_instances.cleaner_ec2_instances_by_tag = mock.Mock()
        walle.clean_ec2_instances('resource', 'account', 'tag')
        assert ec2_instances.cleaner_ec2_instances_by_tag.called

    def test_clean_cloudformation_cleaner_stacks_called(self, tmpdir):
        boto = mock.Mock(BotoConnections)
        dust = tmpdir.mkdir('dust').join('cloudformation_dust')
        dust.write("cloudformation_test")
        walle = WalleConfiguration(boto)
        cloudformation = CleanerCloudFormation
        cloudformation.get_stacks_names = mock.Mock()
        cloudformation.cleaner_stacks = mock.Mock()
        walle.clean_cloudformation('resource', 'account', 'src/dust/cloudformation_dust')
        assert cloudformation.cleaner_stacks.called







