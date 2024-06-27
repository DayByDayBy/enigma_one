class Rotor:
    def __init__(self, wiring, notch):
        self.wiring = wiring    # ie the config, the machine's setting
        self.notch = notch      # ie the notch position - enigma is per-letter, and this alows for movement through those steps
        self.position = 0       # ie the position of the notch, initialised as first notch, 'A'

    def rotate(self):
        self.position = (self.position + 1) % 26

# where the magic happens:
    def encode_forward(self, char):
        # convert char to number (0-25)
        num = ord(char) - ord('A')
        # apply rotor wiring/setting:
        num = (num + self.position) % 26            # ie 0-25, so as to keep within alphabet range
        num = ord(self.wiring[num]) - ord('A')      # applies wiring via set number minus letter-value
        num = (num - self.position + 26) % 26       # reverse position offset
        # convert back to char
        return chr(num + ord('A'))

# where the magic unhappens:
    def encode_backward(self, char):
        # convert char to number (0-25)
        num = ord(char) - ord('A')
        # apply rotor wiring/setting in reverse
        num = (num + self.position) % 26
        num = self.wiring.index(chr(num + ord('A')))
        num = (num - self.position + 26) % 26
        # convert back to char
        return chr(num + ord('A'))

class Reflector:
    def __init__(self, wiring):
        self.wiring = wiring

    def reflect(self, char):
        pass

class Plugboard:
    def __init__(self, connections):
        self.connections = connections

    def swap(self, char):
        pass

class Enigma:
    def __init__(self, rotors, reflector, plugboard):
        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = plugboard

    def encrypt(self, message):
        pass

    def decrypt(self, message):
        pass

def main():
    pass

if __name__ == "__main__":
    main()