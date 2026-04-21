 # funções create_number, create_binary

from ast_nodes.nodes import Number, BinOp

def create_number(value):
    return Number(value)

def create_binary(left, op, right):
    return BinOp(left, op, right)