class Reflector:
    def __init__(self, wiring):
        self.wiring = {}
        for i, char in enumerate(wiring):
            self.wiring[chr(65 + i)] = char
            self.wiring[char] = chr(65 + i)

    def reflect(self, char):    
        return self.wiring[char]