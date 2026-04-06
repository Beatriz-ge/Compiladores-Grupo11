from lexer.tokens import TokenType
from ast.nodes import VarDecl

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise Exception(
                f"Erro: esperado {token_type}, recebeu {self.current_token.type}"
            )

    def parse_declaration(self):
        self.eat(TokenType.INT)

        var_name = self.current_token.value
        self.eat(TokenType.IDENTIFIER)

        value = None

        if self.current_token.type == TokenType.ASSIGN:
            self.eat(TokenType.ASSIGN)
            value = self.current_token.value
            self.eat(TokenType.NUMBER)

        self.eat(TokenType.SEMICOLON)

        return VarDecl(var_name, value)