import logging
from datetime import datetime
from datetime import timedelta

logger = logging.getLogger('Wall-e')


class CleanerSnapshots(object):

    def __init__(self, connection_snapshots):
        self.connection_snapshots = connection_snapshots

    def get_all_snapshots(self):
        return self.connection_snapshots.describe_snapshots()

    def delete_snapshot(self, snapshotId):
        try:
            logger.info('Deleting snapshot: {0}'.format(snapshotId))
            '''
            #result = self.connection_snapshots.delete_snapshot(SnapshotId = snapshotId)
            '''
        except:
            '''
            check if we have to retry due to AWS throttling, fail otherwise
            '''
        else:
            return result

    def cleaner_snapshots_older_than(self, days):
        deleted_snapshots = 0
        snapshots = self.get_all_snapshots()['Snapshots']
        logger.info('Maintaining only snapshots newer than {0} days'.format(str(days)))
        for snapshot in snapshots:
            snapshot_date = snapshot['StartTime']
            tz_info = snapshot_date.tzinfo
            if (datetime.now(tz_info)) > (snapshot_date + timedelta(days=int(days[0]))):
                deleted_snapshots += 1
                logger.info('Deleting snapshot {0} creation date {1}'.format(snapshot['SnapshotId'],snapshot_date))
                '''
                If the snapshot date is greater than the number of days specified, delete it
                # delete_snapshot(snapshot['SnapshotId']
                '''
        logger.info('Total deleted snapshots:{0}'.format(deleted_snapshots))