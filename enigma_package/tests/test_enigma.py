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
        self.enigma.reset()
        decrypted_text = self.enigma.decrypt(ciphertext)
        self.assertEqual(plaintext, decrypted_text)
                
    def test_back_and_forth(self):
        original = "ALAN TURING YET ENDURING"
        encrypted_text = self.enigma.encrypt(original)
        decrypted_text = self.enigma.decrypt(encrypted_text)
        self.assertEqual(original, decrypted_text)
        
 # idempotence is a cool word - it just means the same settings and the same input produce the same output
 # testing that it does change, and that it changes the same text into the same cipher if reset and reprocessed.     
        
    def test_process_idempotence(self):
        plaintext = "THE MEDIUM IS THE MESSAGE"
        first_pass = self.enigma.process(plaintext)     
        self.assertNotEqual(plaintext, first_pass)
        self.enigma.reset()
        second_pass = self.enigma.process(plaintext)
        self.assertEqual(first_pass, second_pass)
        self.enigma.reset()
        third_pass = self.enigma.process(plaintext)
        self.assertEqual(first_pass, third_pass)
            
        

if __name__ == '__main__':
    unittest.main()