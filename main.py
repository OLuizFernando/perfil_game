import pandas as pd
from tkinter import *

AMARELO = '#FBA834'
AZUL = '#387ADF'
AZUL_ESCURO = '#333A73'
AZUL_CLARO = '#50C4ED'

cartas = pd.read_csv('cartas.csv', sep=';')

janela = Tk()

janela.title('Perfil - Python Edition')
janela.resizable(width=FALSE, height=FALSE)
janela.config(pady=50, padx=50, bg=AZUL_ESCURO)

canvas = Canvas(width=520, height=220, bg=AZUL_ESCURO, highlightthickness=0)
canvas.create_text(260, 100, text='PERFIL', fill=AMARELO, font=('Times', 100, 'bold'))
canvas.create_text(260, 175, text='Python Edition', fill=AMARELO, font=('Times', 40))
canvas.grid(column=0, row=0)

botao_iniciar = Button(janela, text='Iniciar', font=('Times', 20, 'bold'),
                       width=10, height=2, foreground=AZUL_ESCURO)
botao_iniciar.grid(column=0, row=1, pady=50)

janela.mainloop()