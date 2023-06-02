def calc(firstvalue, secondvalue, operand):
    if operand == '*':
        output = float(firstvalue) * float(secondvalue)
        print(output)

    elif operand == '+':
        output = float(firstvalue) + float(secondvalue)
        print(output)

    elif operand == '-':
        output = float(firstvalue) - float(secondvalue)
        print(output)

    elif operand == '/':
        output = float(firstvalue) / float(secondvalue)
        print(output)


    elif operand == '%':
        output = float(firstvalue) % float(secondvalue)
        print(output)

    return output

if __name__ == "__main__":
    calc(20, 30, '*')