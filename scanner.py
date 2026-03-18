import re

keywords = {
    'int', 'float', 'return', 'if', 'else', 'while', 'for', 'char','main',
    'double', 'void', 'break', 'continue', 'struct', 'long', 'short',
    'unsigned', 'signed', 'do', 'switch', 'case', 'default', 'typedef', 'const'
}

operators = {'+', '-', '*', '/', '%', '=', '==', '!=', '>', '<', '>=', '<=', '&&', '||', '!', '++', '--'}
separators = {'(', ')', '{', '}', '[', ']', ';', ',', '.'}

identifier_pattern = r'[a-zA-Z_][a-zA-Z0-9_]*'
number_pattern = r'\d+(\.\d+)?'

def lexical_analyzer(code):
    tokens = []

    code = re.sub(r'//.*', '', code)
    code = re.sub(r'/\*[\s\S]*?\*/', '', code)

    parts = re.findall(
        r'[a-zA-Z_][a-zA-Z0-9_]*|\d+\.\d+|\d+|==|!=|>=|<=|&&|\|\||\+\+|--|[+\-*/%=;(),{}[\].<>!]',
        code
    )

    for part in parts:
        if part in keywords:
            tokens.append(f"<KEYWORD, {part}>")
        elif part in operators:
            tokens.append(f"<OPERATOR, {part}>")
        elif part in separators:
            tokens.append(f"<SPECIAL CHARACTER, {part}>")
        elif re.fullmatch(number_pattern, part):
            tokens.append(f"<NUMBER, {part}>")
        elif re.fullmatch(identifier_pattern, part):
            tokens.append(f"<IDENTIFIER, {part}>")
        else:
            tokens.append(f"<UNKNOWN, {part}>")

    return tokens


def main():
    input_file = input("Enter input file path: ").strip()
    output_file = input("Enter output file path: ").strip()

    try:
        with open(input_file, 'r') as f:
            code = f.read()
    except FileNotFoundError:
        print("File not found.")
        return

    tokens = lexical_analyzer(code)

    with open(output_file, 'w') as f:
        for token in tokens:
            f.write(token + "\n")

    print("Done ✔")


if __name__ == "__main__":
    main()