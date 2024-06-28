import unittest
from enigma_machine.reflector import Reflector

class TestReflector(unittest.TestCase):
    def setUp(self):
        self.reflector = Reflector("XNGOKMIEBFZCWVJATYRUHQSLDP")

    def test_reflect(self):
        self.assertEqual(self.reflector.reflect('A'),'X')
        self.assertEqual(self.reflector.reflect('L'),'C')
        self.assertEqual(self.reflector.reflect('Z'),'P')
        

if __name__ == '__main__':
    unittest.main()

