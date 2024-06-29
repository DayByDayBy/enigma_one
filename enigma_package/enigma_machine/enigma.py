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
    
    
    
    
    
    #  wrote out the bones on autopilot a bit, but writing 
    #  tests quickly remembered that enigma is symettrical, 
    #  ie i don't need two functions, just one that can be 
    #  set the same way and work the same way 
    
    # next step (well, sleep, and then) is to flesh this out, but with 
    # a single 'do enigma to it' function, albeit probbaly 
    #  with a more seinseible name, like 'process' or 'transform'