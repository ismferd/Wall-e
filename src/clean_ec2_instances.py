import logging

logger = logging.getLogger('Wall-e')


class CleanerEc2Instances(object):
    def __init__(self, connection_ec2):
        self.connection_ec2 = connection_ec2

    def get_all_ec2_instances_are_running(self):
        return self.connection_ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

    def save_ec2_instances_by_tag(self, tag):
        save_instance = [reservations for reservations in self.get_all_ec2_instances_are_running()
                         for tags in reservations.tags if tags.get('Value') in tag]
        logger.info("Saving ec2 {0} plants".format(save_instance))
        return save_instance

    def cleaner_ec2_instances_by_tag(self, tag):
        all_instances_running = self.get_all_ec2_instances_are_running()
        save_instance = self.save_ec2_instances_by_tag(tag)
        save_instance = [instance for instance in all_instances_running if instance in save_instance]
        for instance in save_instance:
            logger.info("Cleaning ec2 {0} plant".format(instance.instance_id))
            instance.terminate()

