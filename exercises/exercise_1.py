import math

def calculate_area(shape, *args):
    if shape == "square":
        if len(args) == 1:
            return args[0] ** 2
        else:
            return "Invalid number of arguments"
    elif shape == "rectangle":
        if len(args) == 2:
            return args[0] * args[1]
        else:
            return "Invalid number of arguments"
    elif shape == "triangle":
        if len(args) == 2:
            return (args[0] * args[1]) / 2
        else:
            return "Invalid number of arguments"
    elif shape == "circle":
        if len(args) == 1:
            return math.pi * args[0] ** 2
        else:
            return "Invalid number of arguments"
    else:
        return "Unknown shape"

# Unit tests
import unittest

class TestExercise1(unittest.TestCase):

    def test_calculate_area(self):
        self.assertEqual(calculate_area("square", 4), 16)
        self.assertEqual(calculate_area("rectangle", 4, 7), 28)
        self.assertEqual(calculate_area("triangle", 3, 6), 9)
        self.assertAlmostEqual(calculate_area("circle", 3), 28.27, places=2)

if __name__ == '__main__':
    unittest.main()
