import botocore
import logging

logger = logging.getLogger('Wall-e')


class CleanerSnapshots(object):

    def __init__(self, connection_snapshots):
        self.connection_snapshots = connection_snapshots

    def get_all_snapshots(self):
        print("lol")
        return self.connection_snapshots.describe_snapshots()

    def cleaner_snapshots_older_than(self, days):
        snapshots = self.get_all_snapshots()['Snapshots']
        print("days:" + str(days))
        for snapshot in snapshots:
           print(snapshot['SnapshotId']+" "+str(snapshot['StartTime']))