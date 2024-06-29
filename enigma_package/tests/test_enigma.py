import unittest
from enigma_machine.enigma import Enigma

class TestEnigma(unittest.TestCase):
    def setUp(self):
        self.enigma = Enigma() 
        
    def test_encrypt(self):
        plaintext = "HELLO WORLD"
        ciphertext = self.enigma.encrypt(plaintext)
        self.assertIsNotNone(ciphertext)        
        self.assertIsNotEqual(plaintext, ciphertext)
            
    def test_decrypt(self):
        plaintext = "HELLO WORLD"
        ciphertext = self.enigma.encrypt(plaintext)
        decrypted_text = self.enigma.decrypt(ciphertext)
        self.assertEqual(plaintext, decrypted_text)
                
    def test_back_and_forth(self):
        original = "ALAN TURING STANDS ENDURING"
        encrypted_text = self.enigma.encrypt(original)
        decrypted_text = self.enigma.decrypt(encrypted_text)
        self.assertEqual(original, decrypted_text)
        
        

if __name__ == '__main__':
    unittest.main()