import unittest
from enigma_machine.enigma import Enigma
from enigma_machine.rotor import Rotor
from enigma_machine.plugboard import Plugboard
from enigma_machine.reflector import Reflector

class TestEnigma(unittest.TestCase):
    def setUp(self):
        walzen1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
        walzen2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
        walzen3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
        umkehrwalze = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")
        steckerbrett = Plugboard([('A', 'Z'),('G', 'Q'),('L', 'M'),('J', 'F'),('R', 'N'),('O', 'S'),('P', 'D'),('C', 'X')])
        
            
        self.enigma = Enigma(
            [walzen1, 
             walzen2, 
             walzen3], 
            umkehrwalze, 
            steckerbrett) 



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