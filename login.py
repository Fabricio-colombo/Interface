from PySimpleGUI import PySimpleGUI as sg

# Define o tema da interface
sg.theme('DarkAmber')

# Define o layout da janela
layout = [  [sg.Text('Login')],
            [sg.Text('Usuário'), sg.InputText()],
            [sg.Text('Senha'), sg.InputText(password_char='*')],
            [sg.Button('Entrar'), sg.Button('Cancelar')] ]

# Cria a janela
janela = sg.Window('Login', layout)

# Loop de eventos
while True:
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED or evento == 'Cancelar':
        break
    if valores[0] == 'admin' and valores[1] == '1234':
        sg.popup('Login realizado com sucesso!')
        break
    else:
        sg.popup('Usuário ou senha inválidos!')

# Fecha a janela
janela.close()
