import json
from pprint import pprint

from time import sleep
from importlib import import_module
from broccoli.connection import Connection


class BroccoliWorker:

    def __init__(self, host, port, db, name_of_channel, module_name):
        self.module_name = module_name
        self.connection = Connection(host, port, db, name_of_channel)
        self.tasks_dict = {}
        self._fill_tasks_dict()
        pprint(self.tasks_dict)

    def _fill_tasks_dict(self):
        module = import_module(self.module_name)
        for i in module.task_list:
            task_module_name, task_name = i.split('.')
            task_module = import_module(task_module_name)
            task = getattr(task_module, task_name, None)
            if task:
                self.tasks_dict[i] = task

    def _call_task(self, func_name, payload):
        func = self.tasks_dict.get(func_name)
        if not func:
            return
        func(*payload['args'], **payload['kwargs'])

    def run(self):
        while True:
            raw_new_event = self.connection.receive()
            if raw_new_event and raw_new_event['type'] == 'message':
                new_event = json.loads(raw_new_event['data'].decode('utf-8'))
                self._call_task(new_event['name'], new_event['payload'])
            sleep(1)
