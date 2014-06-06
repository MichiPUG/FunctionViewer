from collections import defaultdict

class observers(object):
    def __init__(self):
        self.__registered_clients__ = defaultdict(set)

    def register(self, callback, topic):
        self.__registered_clients__[topic].add(callback)

    def notify(self, topic, *args, **kw):
        for callback in self.__registered_clients__[topic]:
            callback(*args, **kw)

    def registered(self, topic):
        return self.__registered_clients__[topic]
