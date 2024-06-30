class Plugboard:
    def __init__(self, connections):
        
        self.connections = {}
        
        for a, b in connections:
            self.connections[a] = b
            self.connections[b] = a

    def swap(self, char):
        return self.connections.get(char, char)


if __name__ == "__main__":
        
    plugboard = Plugboard(connections=[('A', 'Q'), ('B', 'F')])               
    print(plugboard.swap('A'))
    print(plugboard.swap('B'))
        