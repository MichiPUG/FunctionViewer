
class color_space(object):
    def generate(self, array):
        axes = array.axes
        data = array.data

        for x in xrange(axes[0].count):
          for y in xrange(axes[1].count):
              data[x][y] = 255
  
        return data
    
