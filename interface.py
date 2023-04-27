from PySimpleGUI import PySimpleGUI as sg

#sg.theme_previewer() - olhar todos os temas

sg.theme('DarkBlue16')

layout = [
    [sg.Text('Usuario'), sg.Input(key='usuario', size=(26))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(27))],
    [sg.Checkbox('Salvar Login?')],
    [sg.Button('Entrar')]
]

janela = sg.Window('Tela de Login', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'admin' and valores ['senha'] == '12345':
            print('Login efetuado com sucesso!')