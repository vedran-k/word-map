import unittest
from word_map import WordMap

class TestWordMap(unittest.TestCase):
    def test_initial_letters(self):
        f = open('in1.txt', 'r')
        inLines = f.read().split('\n')
        f.close()
        wm = WordMap(inLines)
        result = wm.traverse()
        self.assertEqual('ACB', result[0])

    def test_initial_path(self):
        f = open('in1.txt', 'r')
        inLines = f.read().split('\n')
        f.close()
        wm = WordMap(inLines)
        result = wm.traverse()
        self.assertEqual('@---A---+|C|+---+|+-B-x', result[1])

    def test_normal_letters(self):
        f = open('in2.txt', 'r')
        inLines = f.read().split('\n')
        f.close()
        wm = WordMap(inLines)
        result = wm.traverse()
        self.assertEqual('ABCD', result[0])

    def test_normal_path(self):
        f = open('in2.txt', 'r')
        inLines = f.read().split('\n')
        f.close()
        wm = WordMap(inLines)
        result = wm.traverse()
        self.assertEqual('@|A+---B--+|+----C|-||+---D--+|x', result[1])

    def test_error_find_starting_direction(self):
        f = open('in3.txt', 'r')
        inLines = f.read().split('\n')
        f.close()
        wm = WordMap(inLines)
        self.assertRaises(Exception, WordMap.find_starting_direction)

if __name__ == '__main__':
    unittest.main()
