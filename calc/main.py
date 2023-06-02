import PySimpleGUI as sg
from calc_functions import calc

sg.theme("Black")

output_box = sg.Text(key="output")

AC = sg.Button("AC", size=[3,1], button_color="White on Black", border_width=0)
Del = sg.Button("Del", size=[3,1], button_color="White on Black", border_width=0)
percentage = sg.Button("%", size=[3,1], button_color="White on Black", border_width=0)
division = sg.Button("/", size=[3,1], button_color="White on Black", border_width=0)

seven = sg.Button("7", size=[3,1], button_color="White on Black", border_width=0)
eight = sg.Button("8", size=[3,1], button_color="White on Black", border_width=0)
nine = sg.Button("9", size=[3,1], button_color="White on Black", border_width=0)
multiply = sg.Button("*", size=[3,1], button_color="White on Black", border_width=0)

four = sg.Button("4", size=[3,1], button_color="White on Black", border_width=0)
five = sg.Button("5", size=[3,1], button_color="White on Black", border_width=0)
six = sg.Button("6", size=[3,1], button_color="White on Black", border_width=0)
minus = sg.Button("-", size=[3,1], button_color="White on Black", border_width=0)

one = sg.Button("1", size=[3,1], button_color="White on Black", border_width=0)
two = sg.Button("2", size=[3,1], button_color="White on Black", border_width=0)
three = sg.Button("3", size=[3,1], button_color="White on Black", border_width=0)
plus = sg.Button("+", size=[3,1], button_color="White on Black", border_width=0)

nil = sg.Button("", size=[3,1], button_color="White on Black", border_width=0)
zero = sg.Button("0", size=[3,1], button_color="White on Black", border_width=0)
fullstop = sg.Button(".", size=[3,1], button_color="White on Black", border_width=0)
output = sg.Button("=", size=[3,1], button_color="White on Black", border_width=0)


window = sg.Window('My To-Do App', layout=[[output_box],
                                           [AC, Del, percentage, division],
                                           [seven, eight, nine, multiply],
                                           [four, five, six, minus],
                                           [one, two, three, plus],
                                           [nil, zero, fullstop, output]])

ar = []

while True:
    event, values = window.read()
    ar.append(event)
    print(ar)
    new_ar = ' '.join(ar)
    window["output"].update(value=new_ar)

    match event:
        case 'AC':
            break

        case 'Del':
            ar = ar[:-2]
            print(ar)
            new_ar = ' '.join(ar)
            window["output"].update(value=new_ar)

        case '':
            ar = ar[:-1]
            print(ar)
            new_ar = ' '.join(ar)
            window["output"].update(value=new_ar)

        case '+':
            new_val = ar.index('+')
            firstvalue = ar[0:new_val]
            firstvalue = ''.join(firstvalue)
            print(firstvalue)

        case '-':
            new_val = ar.index('-')
            firstvalue = ar[0:new_val]
            firstvalue = ''.join(firstvalue)
            print(firstvalue)

        case '*':
            new_val = ar.index('*')
            firstvalue = ar[0:new_val]
            firstvalue = ''.join(firstvalue)
            print(firstvalue)

        case '/':
            new_val = ar.index('/')
            firstvalue = ar[0:new_val]
            firstvalue = ''.join(firstvalue)
            print(firstvalue)

        case '=':
            outputval = ar.index('=')
            secondvalue = ar[new_val:outputval]
            secondvalue = secondvalue[1:]
            secondvalue = ''.join(secondvalue)
            print(secondvalue)
            operand = ar[new_val]
            print(operand)
            final = calc(firstvalue, secondvalue, operand)
            window["output"].update(value=final)
            ar.clear()
            ar = []

window.close()