from collections import defaultdict

class observers(object):
    """Class for different objects to communicate.
    
    Listeners register themselves as such using the register method,
      this requires a topic identifier and a callback function
    Send a messege, consisting of a topic and function parameters,
      by calling the notify method.
    """
    def __init__(self):
        """Create an object of type obervers, no parmeters.
        """
        self.__registered_clients__ = defaultdict(set)

    def register(self, callback, topic):
        """Register a listener for topic 
        callback = callback function, function is called to notify listener
        topic = channel identfier
        """
        self.__registered_clients__[topic].add(callback)

    def notify(self, topic, *args, **kw):
        """Send message to registered listeners
        topic = channel identfier
        *args, **kw = parameters to pass to callfack function
        """
        for callback in self.__registered_clients__[topic]: #For each listener
            callback(*args, **kw) #Send message

    def registered(self, topic):
        """Return list of listeners for a topic
        topic = channel identfier
        """
        return self.__registered_clients__[topic]
