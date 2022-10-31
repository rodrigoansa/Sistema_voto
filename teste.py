from PySimpleGUI import Window, Button, Text, Image, Input

#Fotos


#Layout
layout = [
    [Image(filename='xuxa.png')]

]
window = Window(
    'Janela',
    layout=layout
)

print(window.read())

window.close()