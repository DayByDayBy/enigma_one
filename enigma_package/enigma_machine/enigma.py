class Enigma:
    def __init__(self, rotors, reflector, plugboard):
        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = plugboard
        
    def reset(self):
        for rotor in self.rotors:
            rotor.reset()    

    def encrypt(self, message):
        pass

    def decrypt(self, message):
        pass