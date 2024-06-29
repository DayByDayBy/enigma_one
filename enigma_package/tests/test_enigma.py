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
        
    # none of that needed to be in german, i know. but steckerbrett is a cooler word than plugboard
            
        self.enigma = Enigma(
            [walzen1, 
             walzen2, 
             walzen3], 
            umkehrwalze, 
            steckerbrett) 



    def test_encrypt(self):
        plaintext = "HELLO WORLD"
        ciphertext = self.enigma.process(plaintext)
        self.assertIsNotNone(ciphertext)        
        self.assertNotEqual(plaintext, ciphertext)
            
    def test_decrypt(self):
        plaintext = "HELLO WORLD"
        ciphertext = self.enigma.process(plaintext)
        self.enigma.reset()
        decrypted_text = self.enigma.process(ciphertext)
        self.assertEqual(plaintext, decrypted_text)
                
    def test_back_and_forth(self):
        original = "ALAN TURING YET ENDURING"
        encrypted_text = self.enigma.process(original)
        self.enigma.reset()
        decrypted_text = self.enigma.process(encrypted_text)
        self.assertEqual(original, decrypted_text)
        
    def test_empty_string(self):
        self.assertEqual(self.enigma.process(""), "")
        
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
            
            
            
            
            
            
            
    # def test_different_config(self):
    
    
    
    #         self.enigma = Enigma(
    #         [walzen1, 
    #          walzen2, 
    #          walzen3], 
    #         umkehrwalze, 
    #         steckerbrett) 
    

if __name__ == '__main__':
    unittest.main()