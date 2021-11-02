from tkinter import *
from tkinter import ttk
import random

def main():
    root = Tk()

    frame1 = ttk.Frame(root,padding=100)
    frame1.grid()

    botaoprint = ttk.Button(frame1,text="print de algo")
    botaoprint['command'] = (lambda:
                             printrando()) # Aqui nós usamos o comando de dicionario [command] para sinalizar que algo vai acontecer 
                                           # Quando este botão ser apertado. O lambda diz que oq acontecer no lado direito (printrando())
                                           # Vai ser imposto ao botão definido como botaoprint

    botaoprint.grid()

    root.mainloop()

def printrando():
    letras = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z')
    letrarando = ''

    for _ in range(10):
        letra = letras[random.randrange(26)]
        letrarando = letrarando + letra

    print(letrarando)
# Oque esta função faz é que quando o botão é apertado, o programa pega 10 letras aleatorias das 26 e joga num print para o console.

main()

# Basicamente mesmos comentarios do arquivo frame_button.py