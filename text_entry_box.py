# objeto copiado para teste e estudo

"""from tkinter import *
from tkinter import ttk

def main():
    root = Tk()

    frame1 = ttk.Frame(root)
    frame1.grid()

    my_entry_box = ttk.Entry(frame1)
    my_entry_box.grid()

    texto_entry_button = ttk.Button(frame1,text='Print entry')
    texto_entry_button['command'] = (lambda: 
                                     print_contents(my_entry_box))

    texto_entry_button.grid()

    root.mainloop()

def print_contents(entry_box):
    conteudo_da_caixa = entry_box.get()
    print(conteudo_da_caixa)
main()"""

#feito sozinho
from tkinter import *
from tkinter import ttk

def main():
    root = Tk()

    frame1 = ttk.Frame(root)
    frame1.grid()

    caixa_de_texto = ttk.Entry(frame1) # Entry é uma caixa para digitar. Usando isso conseguimos digitar algo neste espaço
                                       # e printar ou qualquer coisa do tipo. 
    caixa_de_texto.grid()

    botao_caixa_de_texto = ttk.Button(frame1,text='Ain')
    botao_caixa_de_texto['command'] = (lambda: print_da_caixa(caixa_de_texto)) # Aqui eu crio uma função chamada print_da_caixa 
                                                                               # e nela atribuo minha entry_box(caixa_de_texto)
                                                                               # assim tudo oque eu digito na caixa, após apertar o botão
                                                                               # o mesmo é printado na tela.
    botao_caixa_de_texto.grid()

    root.mainloop()

def print_da_caixa(entry_box): #crio o parametro entry_box
    conteudo_da_caixa = entry_box.get() #pego oque for atribuido a este parametro
    print(conteudo_da_caixa) # printo no console oque foi digitado
    # tudo isso após clicar no botao (botao_caixa_de_texto)

main()