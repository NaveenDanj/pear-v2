import uuid

class Line:
    def __init__(self , line ,lm):
        self.raw_line = line
        self.line_number = lm
        self.line = []

class Statement:

    def __init__(self , raw_statement , splitted ):
        self.raw_statement = raw_statement
        self.splitted = splitted
        self.pointer = None
        self.white_space_before = 0
        self.next = None
        self.prev_pointer = None
        self.root_pointer = None
        self.nested_id = uuid.uuid1()

class IfStatement(Statement):

    def __init__(self , raw_statement , splitted):
        super(raw_statement , splitted)
        self.true_pointer = None
        self.false_pointer = None


class Token:

    def __init__(self , type , ):
        pass
