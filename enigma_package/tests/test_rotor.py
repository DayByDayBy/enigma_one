import unittest
from enigma_machine.main import Rotor

class TestRotor(unittest.TestCase):
    def setUp(self):
        self.rotor = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 'Q')

    def test_encode_forward(self):
        self.assertEqual(self.rotor.encode_forward('A'), 'E')
        self.assertEqual(self.rotor.encode_forward('Z'), 'J')
        # Add more test cases for different characters and positions

    def test_encode_backward(self):
        self.assertEqual(self.rotor.encode_backward('E'), 'A')
        self.assertEqual(self.rotor.encode_backward('J'), 'Z')
        # Add more test cases for different characters and positions

if __name__ == '__main__':
    unittest.main()
