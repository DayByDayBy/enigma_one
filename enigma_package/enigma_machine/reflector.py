class Reflector:
    def __init__(self, wiring):
        self.wiring = wiring

    def reflect(self, char):
        idx = ord(char) - ord('A')
        return self.wiring[idx]
        
