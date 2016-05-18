#!/usr/bin/python


class CleanerCloudFormation(object):

    def __init__(self, connection_cloudformation):
        self.connection_cloudformation = connection_cloudformation

    def get_all_stacks(self):
        list_stacks = self.connection_cloudformation.stacks.all()
        return list_stacks

    def get_stacks_names(self):
        object_stack = self.get_all_stacks()
        stacks_name = list()
        for stack in object_stack:
            stacks_name.append(stack.stack_name)
        return stacks_name

    def cleaner_stacks(self, cf_dust_not_clean):
        stacks_name = self.get_stacks_names()
        for stack in stacks_name:
            if stack not in cf_dust_not_clean:
                try:
                    print stack
                   #self.connection_cloudformation.delete_stack(stack)
                except Exception, err:
                        print "Oops!  The stack have problem for die.  Try again..."
                        print err



