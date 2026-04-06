from lexer.lexer import Lexer
from parser.parser import Parser

def main():
    code = "int x = 10;"

    lexer = Lexer(code)
    parser = Parser(lexer)

    result = parser.parse_declaration()

    print(result)


if __name__ == "__main__":
    main()