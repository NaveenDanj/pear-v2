
class Line:
    def __init__(self , line ,lm):
        self.raw_line = line
        self.line_number = lm
        self.line = []

class Statement:

    def __init__(self , raw_statement , splitted ):
        self.nextStatement = None
        self.raw_statement = raw_statement
        self.splitted = splitted
        self.identifier = None
        self.pointer = None


class Token:

    def __init__(self , type , ):
        pass
