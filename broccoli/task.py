import json
from uuid import uuid4


class Task:

    def __init__(self, func, name: str, connection):
        self.connection = connection
        self.func = func
        self.name = name

    def __call__(self, *args, **kwargs):
        self.func(*args, **kwargs)

    def delay(self, *args, **kwargs):
        self.connection.send(
            json.dumps({
                'id': str(uuid4()),
                'name': self.name,
                'payload': {
                    'args': args,
                    'kwargs': kwargs
                }
            })
        )