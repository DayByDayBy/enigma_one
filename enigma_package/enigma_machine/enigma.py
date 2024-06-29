from enigma_machine.rotor import Rotor
from enigma_machine.plugboard import Plugboard
from enigma_machine.reflector import Reflector


class Enigma:
    def __init__(self, rotors, reflector, plugboard):
        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = plugboard
        
    def reset(self):
        for rotor in self.rotors:
            rotor.reset()    

    # def encrypt(self, message):
    #     pass

    # def decrypt(self, message):
    #     pass
    
   
    # getting a bit distracted atm by what to do with spaces 
    # etc - enigma OG only had A-Z keys, and would output an 
    # unbroken string of A-Z only which would then be tapped 
    # out as if a sequence of 5 letter words (as convention, sometimes 4, could be any number)
    
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
                
            char = self.relfector.reflect(char)
            
            for rotor in reversed(self.rotors):
                char = rotor.encode_backward(char)
            char = self.plugboard.swap(char)
            
            result += char
        return result 
    
    
    
    
    
    
    
    
    #  wrote out the bones on autopilot a bit, but writing 
    #  tests quickly remembered that enigma is symettrical, 
    #  ie i don't need two functions, just one that can be 
    #  set the same way and then work the same way; 
    #  plaintext becomes cipher, cipher becomes plaintext
    
    #  next step (well, sleep, and then) is to flesh this out, but with 
    #  a single 'do enigma to it' function, albeit probbaly 
    #  with a more seinseible name, like 'process' or 'transform'