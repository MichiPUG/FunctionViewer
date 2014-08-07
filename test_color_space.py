from color_space import color_space
from array import axis, array

import unittest

class test_colorspace(unittest.TestCase):
    def test_create(self):
        obj = color_space()
        self.assertTrue(isinstance(obj, color_space))

    def test_axis(self):
        obj = axis('x', 0, 16, 1)
        self.assertEqual(obj.name, 'x')
        self.assertEqual(obj.min_value, 0)
        self.assertEqual(obj.max_value, 16)
        self.assertEqual(obj.step, 1)

    def test_array(self):
        axes = [axis('x', 0, 15, 1), axis('y', 0, 15, 1)]
        data = array(axes, color_space)
        self.assertEqual(len(data.axes), 2)


    def test_generate(self):
        data = array([axis('x', 0, 15, 1), axis('y', 0, 15, 1)], color_space)
        new_data = data.step()
        errors = 0
        value = new_data
        for x in xrange(data.axes[0].count):
            for y in xrange(data.axes[1].count):
                if value[x][y] != 255:
                    errors += 1
        self.assertEqual(errors, 0)
        

