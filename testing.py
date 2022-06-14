""" Add a test for notable functions bellow """

import unittest
import functions as f


class FunctionTesting(unittest.TestCase):
    
    def test_take_move(self):
        old = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        new = [0, 1, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(f.take_move(old, 1, 2), new)

    def test_update(self):
        data = [1, 1, 2, 0, 2, 0, 0, 0, 0]
        visual = ['X', 'X', 'O', '_', 'O', '_', '_', '_', '_']
        self.assertEqual(f.update(data), visual)

    # def test_win_check(self):
    #     x_win = [1, 1, 1, 0, 2, 0, 0, 0, 2]
    #     self.assertEqual(f.win_check(x_win), 1)

if __name__ == '__main__':
    unittest.main()
