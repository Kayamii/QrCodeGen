import qrcode
import os
import PySimpleGUI as sg


event, (input,) = sg.Window('QR Code Generator', [[sg.Text('Enter a link:'), sg.InputText()], [sg.Button('Ok')]]).read(close=True)
img = qrcode.make(input)
type(img)
img.save("input.png")
