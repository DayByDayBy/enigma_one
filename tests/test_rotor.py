import unittest
from enigma_machine.rotor import Rotor

class TestRotor(unittest.TestCase):
    def setUp(self):
        self.rotor = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 'Q')

    def test_encode_forward(self):
        self.assertEqual(self.rotor.encode_forward('A'), 'E')
        self.assertEqual(self.rotor.encode_forward('Z'), 'J')

    def test_encode_backward(self):
        self.assertEqual(self.rotor.encode_backward('E'), 'A')
        self.assertEqual(self.rotor.encode_backward('J'), 'Z')

if __name__ == '__main__':
    unittest.main()

