def string_format(number):
    width = len(bin(number)[2:])
    formatted_strings = []
    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]
        formatted_strings.append(f"{decimal:>{width}} {octal:>{width}} {hexadecimal:>{width}} {binary:>{width}}")
    return '\n'.join(formatted_strings)