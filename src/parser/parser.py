from lexer.tokens import TokenType
from ast_nodes.nodes import VarDecl, Return


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

    def parse_return(self):
        self.eat(TokenType.RETURN)

        value = None

        # pode ser número ou identificador
        if self.current_token.type == TokenType.NUMBER:
            value = self.current_token.value
            self.eat(TokenType.NUMBER)

        elif self.current_token.type == TokenType.IDENTIFIER:
            value = self.current_token.value
            self.eat(TokenType.IDENTIFIER)

        else:
            raise Exception("Erro: return precisa de um valor válido")

        self.eat(TokenType.SEMICOLON)

        return Return(value)