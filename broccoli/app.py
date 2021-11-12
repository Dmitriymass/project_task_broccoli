from broccoli.connection import Connection
from broccoli.task import Task


class Broccoli:

    def __init__(self, host, port, db, name_of_channel):
        self.connection = Connection(host, port, db, name_of_channel)

    def as_task(self, func, name):
        task = Task(func, name, self.connection)
        return task