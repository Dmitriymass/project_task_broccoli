import redis


class Connection:

    def __init__(self, host, port, db, name_of_channel):
        self.queue = redis.StrictRedis(host=host, port=port, db=db)
        self.channel = self.queue.pubsub()
        self.name_of_channel = name_of_channel
        self.channel.subscribe(self.name_of_channel)

    def send(self, body):
        self.queue.publish(self.name_of_channel, body)

    def receive(self):
        return self.channel.get_message()
