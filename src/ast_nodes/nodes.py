# definição dos nós da AST

class Number:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Number({self.value})"


class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op          # Token
        self.right = right

    def __repr__(self):
        return f"Binary({self.left} {self.op.type.name} {self.right})"


class VarDecl:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"VarDecl(name={self.name}, value={self.value})"


class Return:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Return(value={self.value})"


class Block:
    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return f"Block(statements={self.statements})"


class MainNode:
    def __init__(self, body):
        self.body = body

    def __repr__(self):
        return f"MainNode(body={self.body})"

class Program:
    def __init__(self, functions):
        self.functions = functions  # Uma lista de FunctionNode

    def __repr__(self):
        return f"Program(functions={self.functions})"

class Function:
    def __init__(self, return_type, name, parameters, body):
        self.return_type = return_type
        self.name = name
        self.parameters = parameters 
        self.body = body            

    def __repr__(self):
        return f"Function(name={self.name}, return={self.return_type}, body={self.body})"