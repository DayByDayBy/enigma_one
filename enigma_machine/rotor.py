# walzen:
class Rotor:
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def __init__(
        self, 
        wiring, 
        notch, 
        initial_position = 'A'
        ): 
        
        self.wiring = wiring                                        # ie the config, the machine's setting
        self.notch = notch                                      
        self.initial_position = self.ALPHABET.index(initial_position.upper())
        self.position = self.initial_position


    def encode_forward(self, char):
        shift = (ord(char)- ord('A') + self.position)% 26
        return self.wiring(shift)
    def encode_backward(self, char):
        shift = (self.reverse_wiring[char] - self.position + 26) % 26
        return chr(shift + ord('A'))

    def rotate(self):
        self.position = (self.position + 1) % 26
        return self.position == self.notch