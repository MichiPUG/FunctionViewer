class axis(object):
    def __init__(self, name, min_value, max_value, step):
        self.name = name
        self.min_value = min_value
        self.max_value = max_value
        self.step = step
        self.count = (max_value - min_value) / step + 1


class array(object):

    def __init__(self, axes, generator):
        self.axes = axes
        self.generator = generator()
        self.data = self.create_empty()

    def step(self):
        return self.generator.generate(self)

    def create_empty(self):
        return [list(None for dummy_1 in xrange(self.axes[1].count))
          for dummy in xrange(self.axes[0].count)]
        


