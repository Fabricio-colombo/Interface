from PySimpleGUI import PySimpleGUI as sg

#layout
sg.theme('Dark Amber 5')
layout = [
    [sg.Text('Login'), sg.Input(key='login', size=(24, 1))],
    [sg.Text('Password'), sg.Input(key='password', password_char='*', size=(20, 1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Enter')]
]

#janelas
janela = sg.Window('Account', layout)

#ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Enter':
        if valores['login'] == 'fabricio' and valores ['password'] == 'fabricio12345':
            print('Welcome to you account!')