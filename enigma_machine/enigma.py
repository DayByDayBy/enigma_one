from enigma_machine.rotor import Rotor
from enigma_machine.plugboard import Plugboard
from enigma_machine.reflector import Reflector



# walzen1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
# walzen2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE")
# walzen3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO")
# umkehrwalze = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")
# steckerbrett = Plugboard([('A', 'Z'),('G', 'Q'),('L', 'M'),('J', 'F'),('R', 'N'),('O', 'S'),('P', 'D'),('C', 'X')])

class Enigma:
    def __init__(self, rotors, reflector, plugboard):
        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = plugboard
   

    # def encrypt(self, message):
    #     pass

    # def decrypt(self, message):
    #     pass
    
    # getting a bit distracted atm by what to do with spaces 
    # etc - enigma OG only had A-Z keys, and would output an 
    # unbroken string of A-Z only which would then be tapped 
    # out as if a sequence of 5 letter words (as convention, 
    # sometimes 4, could be any number) which seems like an 
    # okay way to avoid making frequency and spacing analysis 
    # harder, but i wonder if a method that encrypted spaces 
    # too would be worth investigating - a 27 character alphabet, 
    # as it were, where a space might be swapped for a letter, and 
    # a letter might be swapped for a space. same logic could be 
    # applied to a period, etc
    
    
    def process(self, message):
        result = ""
        for char in message:
            if char == ' ':
                result += ' '
                continue
            
            char = self.plugboard.swap(char)
            
            for rotor in self.rotors:
                rotor.rotate()
                char = rotor.encode_forward(char)
                
            char = self.reflector.reflect(char)
            
            for rotor in reversed(self.rotors):
                char = rotor.encode_backward(char)
            char = self.plugboard.swap(char)
            
            result += char
        return result 
    
    
    def reset(self):
        for rotor in self.rotors:
            rotor.reset()    



