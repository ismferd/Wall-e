import botocore
import logging

logger = logging.getLogger('Wall-e')


class CleanerSnapshots(object):

    def __init__(self, connection_snapshots):
        self.connection_snapshots = connection_snapshots

    def get_all_snapshots(self):
        return self.connection_snapshots.describe_snapshots()['SnapshotIds']

    def cleaner_snapshots(self):
        snapshots = self.get_all_snapshots()

        for snapshot in snapshots:
           print snapshot