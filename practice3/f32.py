class C32:
    def __init__(self):
        self.condition = 'A'
    def slur(self):
        if self.condition == 'A':
            self.condition = 'B'
            return 0
        elif self.condition == 'B':
            self.condition = 'C'
            return 1
        elif self.condition == 'C':
            self.condition = 'D'
            return 2
        elif self.condition == 'D':
            self.condition = 'G'
            return 4
        elif self.condition == 'E':
            self.condition = 'F'
            return 5
        elif self.condition == 'H':
            self.condition = 'E'
            return 11
        else:
            RuntimeError
            
    def order(self):
        if self.condition == 'D':
            self.condition = 'E'
            return 3
        elif self.condition == 'E':
            self.condition = 'G'
            return 7
        elif self.condition == 'F':
            self.condition = 'G'
            return 8
        elif self.condition == 'G':
            self.condition = 'H'
            return 9
        elif self.condition == 'H':
            self.condition = 'C'
            return 10

        else:
            RuntimeError

    def stay(self):
        if self.condition == 'E':
            self.condition = 'A'
            return 6
        else:
            RuntimeError
