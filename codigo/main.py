# importando biblioteca tkinter
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# importando pillow

from PIL import ImageTK, imagem

# cores

co0 = '#2e2d2b' # Preta
co1 = '#feffff' # Branca
co2 = '#e5e5e5' # branca
co3 = '#00a005' # Verde
co4 = '#403d3d' # letra
co6 = '#003452' # azul escuro
co7 = '#ef5350' # vermelha

co6 = '#038cfc' # azul
co8 = '#263238' # + verde escuro
co9 = '#e9edf5' # + verde

# Criando janela
janela = Tk()
janela.title("")
janela.geometry('850x620')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use('clam')

# Criando Frames

#Faixa azul do cabeçalho
frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

# linha abaixo do cabeçalho e segundo frames
ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_dados = Frame(janela, width=850, height=65, bg=co1)
frame_dados.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_detalhes = Frame(janela, width=850, height=200, bg=co1)
frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

# FTrabalhando no frame Logo -----------------




janela.mainloop()

