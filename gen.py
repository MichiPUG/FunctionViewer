class axis(object):

    def __init__(self, name, min, max, step):
        self.name = name
        self.min = min
        self.max = max
        self.step = step


class array_manager(object):

    def __init__(self, axes, generate):
        self.axes = axes
        self.generate = generate

    def step(self):
       self.generate()
       return array





class generate_2d(object):
  "fills in array with data to be displays"
  
  def generate(data):
    for x in xrange(data.x_min, data.x_max, data.x_step):
        for y in xrange(data.y_min, data.y_max, data.y_step):
            data.data[x][y] = self.function(x, y, data)
    



class color_space(generate_2d):

    def function(self, x, y, data):
      return 255


  


