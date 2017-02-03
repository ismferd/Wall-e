import logging

logger = logging.getLogger('Wall-e')

class StsInfo(object):

    def __init__(self, connection_sts):
        self.connection_sts = connection_sts

    def get_sts_info(self):
        print(self.connection_sts.get_caller_identity()['Account'])
        return self.connection_sts.get_caller_identity()['Account']


