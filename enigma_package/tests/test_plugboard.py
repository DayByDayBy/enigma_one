import unittest
from enigma_machine.plugboard import Plugboard

class TestPlugboard(unittest.TestCase):
    def setUp(self):
        self.plugboard = Plugboard(connections=(('A', 'Q'),('B', 'F'))) 

    def test_swap(self):
        self.assertEqual(self.plugboard.swap('A'), 'Q')
        self.assertEqual(self.plugboard.swap('B'), 'F')
        self.assertEqual(self.plugboard.swap('C'), 'C') # disconnected, ie no change

if __name__ == '__main__':
    unittest.main()