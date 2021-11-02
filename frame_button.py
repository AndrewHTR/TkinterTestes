from tkinter import *
from tkinter import ttk

def main():
    root = Tk() # Constroi os atributos da classe tkinter.Tk. É comumente chamado de root.

    frame1 = ttk.Frame(root,padding=100) # aqui nós construimos um widget (widget é tudo oque há na tela.) dando o nome de frame1 para uso subsequente.
    #usamos frames para agrupar nossos itens como: botões, textos e etc... 
    frame1.grid() # Mostra o Frame usando o layout 'grid' do tkinter. Mais tarde aprender sobre como manipular o layout

    botaoavancar = ttk.Button(frame1,text="Avançar",padding=10) # Constroi um widget ttk.Button com o nome Avançar (este é o botão que aparecerá na tela)
    botaoavancar.grid() #Mostra o Botão usando o layout 'grid' do tkinter.

    botao2 = ttk.Button(frame1,text='Alo',padding=20)
    botao2.grid()

    root.mainloop() # inicia o loop. O programa será fechado apenas quando o usuario quiser.

main() #chamo a função

#####################################################################################################################################
#
# O que acontece aqui é que primeiro:
#
# Nós importamos a biblioteca do Tkinter
#
# Depois criamos o nosso frame1 (ttk.Frame) que é onde agruparemos nossos itens, cada frame é uma janela diferente.
# em seguida mostramos na tela utilizando o grid do tkinter
#
# Após isso criamos um botão no nosso frame1(lembrando que é lá onde agrupamos nossos itens.) e damos o texto "Avançar"
# e o tamanho(preenchimento) de 10 pixels.
#
# Em seguida fazemos o mesmo que com o frame1, colocamos ele na grid para que seja mostrado na tela.
#
# e por ultimo iniciamos o loop para que a janela feche somente quando o usuario quiser.
#
#####################################################################################################################################