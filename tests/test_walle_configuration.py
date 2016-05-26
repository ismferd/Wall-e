#from src.wall_e import WalleConfiguration
#import mock
#
#
#class TestWalleConfiguration(object):
#     def test_clean_cloudformation_cleaner_stacks_is_called(self, tmpdir):
#         mock_dust_file = tmpdir.mkdir("files").join("cloudformation")
#         mock_dust_file.write('{0}\n{1}'.format('cloudformation', 'cloudformation2'))
#         mock_connection = mock.Mock()
#         walle_configuration = WalleConfiguration(str(mock_dust_file.realpath()), mock_connection)
#         walle_configuration.cformation.cleaner_stacks = mock.Mock()
#         walle_configuration.clean_cloudformation()
#         walle_configuration.cformation.cleaner_stacks.called
#
#
