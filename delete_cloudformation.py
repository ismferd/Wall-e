#!/usr/bin/python
import time

class DeleteCloudFormation(object):

    def __init__(self, connection_cloudformation):
        self.connection_cloudformation = connection_cloudformation

    def get_all_stacks(self):
        list_stacks = self.connection_cloudformation.describe_stacks()
        return list_stacks

    def get_stacks_names(self):
        object_stack = self.get_all_stacks()
        stacks_name = list()
        for stack in object_stack:
            stack_name = stack.stack_name
            stacks_name.append(stack_name)
        return stacks_name

    def delete_stacks(self, stacks_not_die):
        stacks_name = self.get_stacks_names()
        for stack in stacks_name:
            if stack not in stacks_not_die:
                try:
                   # self.connection_cloudformation.delete_stack(stack)
                except Exception,e:
                        print "Oops!  The stack have problem for die.  Try again..."
                        print e
                        time.sleep(10)



