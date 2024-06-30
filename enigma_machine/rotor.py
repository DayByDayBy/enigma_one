# walzen:
class Rotor:
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def __init__(
        self, 
        wiring, 
        notch, 
        position = 'A'
        ): 
        
        self.wiring = wiring 
        self.reverse_wiring = {V: k for k, V in enumerate(wiring)}
        self.notch = ord(notch) - ord('A')                                      
        self.position = ord(position) - ord('A')

    def encode_forward(self, char):
        shift = (ord(char)- ord('A') + self.position)% 26
        encoded_char = self.wiring[shift]
        return encoded_char
    
    def encode_backward(self, char):
        shift = (self.reverse_wiring[char] - self.position + 26) % 26
        return chr(shift + ord('A'))

    def rotate(self):
        self.position = (self.position + 1) % 26
        return self.position == self.notch