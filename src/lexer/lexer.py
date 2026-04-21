from .tokens import TokenType, Token

class Lexer:
    def __init__(self, source):
        self.source = source
        self.pos = 0

        self.line = 1
        self.column = 1

        self.current_char = self.source[self.pos] if source else None

    # Avança caractere (controle correto de linha/coluna)
    def advance(self):
        if self.current_char == "\n":
            self.line += 1
            self.column = 1
        else:
            self.column += 1

        self.pos += 1

        if self.pos < len(self.source):
            self.current_char = self.source[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            self.advance()

    # 🔹 Método padrão para criar tokens (SEMPRE usar)
    def make_token(self, type, value=None, line=None, column=None):
        token = Token(
            type,
            value,
            line if line is not None else self.line,
            column if column is not None else self.column
        )

        if hasattr(self, "debug") and self.debug:
            print(f"[TOKEN] {token}")

        return token

    def number(self):
        start_line = self.line
        start_column = self.column

        result = ""

        while self.current_char and self.current_char.isdigit():
            result += self.current_char
            self.advance()

        return self.make_token(TokenType.NUMBER, int(result), start_line, start_column)

    def identifier(self):
        start_line = self.line
        start_column = self.column

        result = ""

        while self.current_char and (
            self.current_char.isalnum() or self.current_char == "_"
        ):
            result += self.current_char
            self.advance()

        if result == "int":
            return self.make_token(TokenType.INT, None, start_line, start_column)
        elif result == "return":
            return self.make_token(TokenType.RETURN, None, start_line, start_column)

        return self.make_token(TokenType.IDENTIFIER, result, start_line, start_column)

    def get_next_token(self):
        while self.current_char:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return self.number()

            if self.current_char.isalpha() or self.current_char == "_":
                return self.identifier()

            # 🔹 operadores e símbolos (posição correta)
            if self.current_char == "=":
                token = self.make_token(TokenType.ASSIGN)
                self.advance()
                return token

            if self.current_char == ";":
                token = self.make_token(TokenType.SEMICOLON)
                self.advance()
                return token

            if self.current_char == "(":
                token = self.make_token(TokenType.LPAREN)
                self.advance()
                return token

            if self.current_char == ")":
                token = self.make_token(TokenType.RPAREN)
                self.advance()
                return token

            if self.current_char == "{":
                token = self.make_token(TokenType.LBRACE)
                self.advance()
                return token

            if self.current_char == "}":
                token = self.make_token(TokenType.RBRACE)
                self.advance()
                return token

            if self.current_char == "+":
                token = self.make_token(TokenType.PLUS)
                self.advance()
                return token

            if self.current_char == "-":
                token = self.make_token(TokenType.MINUS)
                self.advance()
                return token

            if self.current_char == "*":
                token = self.make_token(TokenType.MULT)
                self.advance()
                return token

            if self.current_char == "/":
                token = self.make_token(TokenType.DIV)
                self.advance()
                return token

            raise Exception(f"Caractere inválido: {self.current_char}")

        return self.make_token(TokenType.EOF)
    
