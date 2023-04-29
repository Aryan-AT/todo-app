import PySimpleGUI as sg
import coding.ex_function

label1 = sg.Text("Enter feet: ")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter inches: ")
input2 = sg.Input(key="inches")

button = sg.Button("Convert")

window = sg.Window("Converter", layout=[[label1,input1],[label2,input2], [button]])

while True:
    event, values = window.read()
    print(event)
    print(values)

window.read()
window.close()