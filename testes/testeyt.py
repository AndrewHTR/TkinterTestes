from tkinter import *
from tkinter import ttk
import pytube

def main():
    root = Tk()

    frame1 = ttk.Frame(root,padding=100)
    frame1.grid()

    caixinhadownload = ttk.Entry(frame1)
    caixinhadownload.grid()

    botaodownload = ttk.Button(frame1,text='Download')
    botaodownload['command'] = (lambda: downloadyt(caixinhadownload))
    botaodownload.grid()
    
    root.mainloop()


def downloadyt(entry_box):

    url = entry_box.get()

    yt = pytube.YouTube(url)

    print(f'O video está sendo baixado: {yt.title}')

    video = yt.streams.get_by_itag(22)

    video.download(output_path='./tkinterzada/downloadsyt')
    video.on_complete(print('O download foi concluido!'))
    print('Descrição do video:\n')
    print(yt.description)
    """print(yt.streams)
    print(yt.streams.filter(file_extension='mp4'))c:\\Users\\andre\\Documents\\Python\\Estudos\\tkinterzada\\downloadsyt\\"""

main()