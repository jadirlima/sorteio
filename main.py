import pandas as pd
import random
from tkinter import *
from tkinter.constants import DISABLED, NORMAL
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


root = Tk()
photo = PhotoImage(file = "logo_b.png")
root.iconphoto(False, photo)

class app():
    def __init__(self):
        self.root = root
        self.janela()
        root.mainloop()

    def janela(self):
        self.root.title("   Sorteador PMBV V1.5")
        self.root.configure(background='#87CEFA')
        self.root.geometry("700x600")
        self.frames_da_janela()
        self.root.resizable(False, False)

    def frames_da_janela(self):

        self.frame_1 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=2)
        self.frame_1.place(relx=0.02, rely=0.05, relwidth=0.96, relheight=0.93)

        back = Label(self.root)
        back.la = PhotoImage(file='logo_b.png')
        back['image'] = back.la
        back.place(relx=0.23, rely=0.55)

        titulo = Label(self.root, text="Sorteio Prefeitura Municipal de Boa Vista",
                       fg="SteelBlue", bg='#dfe3ee', justify='center', font=("Arial", 12,'bold'))
        titulo.place(relx=0.15, rely=0.09, relwidth=0.7)

        open_button = Button(self.root, text='Localizar arquivo', bd=2, bg='#4682B4', fg='White',
                                   font=('verdana', 8, 'bold'), command=self.select_file)
        open_button.place(relx=0.2, rely=0.2, height=20)

        self.pp1 = StringVar()
        self.pp1.set("super_herois.xlsx")
        self.pp1_entry = Entry(self.root, textvariable=self.pp1, justify='center', state=DISABLED)
        self.pp1_entry.place(relx=0.4, rely=0.2, relwidth=0.25, height=20)
        self.bt_calcular1 = Button(self.root, text="Sortear", bd=2, bg='#4682B4', fg='White',
                                   font=('verdana', 10, 'bold'),  state=NORMAL, command=self.butaoclick1)
        self.bt_calcular1.place(relx=0.15, rely=0.25, relwidth=0.35, relheight=0.07)

        self.bt_calcular2 = Button(self.root, text="Resetar", bd=2, bg='#4682B4', fg='White',
                                   font=('verdana', 10, 'bold'), command=self.apagar)
        self.bt_calcular2.place(relx=0.55, rely=0.25, relwidth=0.35, relheight=0.07)

        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=2)
        self.frame_2.place(relx=0.09, rely=0.4, relwidth=0.8, relheight=0.15)

        self.resultado = StringVar()
        self.apagar()
        self.resultado1 = Label(self.root, textvariable=self.resultado,
                                fg="Gold", bg='#778899', justify="left", font=("Arial",14,'bold'))
        self.resultado1.place(relx=0.15, rely=0.45, relwidth=0.7)




    def apagar(self):
        self.bt_calcular1['state'] = NORMAL
        return self.resultado.set("-----------------------------------------------------")

    def butaoclick1(self):
        # sleep(1)
        arquivo = self.pp1.get()
        try:
            servidores = pd.read_excel(arquivo)
            lista_servidores = servidores['nome']
            self.bt_calcular1['state'] = DISABLED
            return self.resultado.set(lista_servidores[random.randrange(len(lista_servidores))])
        except SystemExit:
            raise
        except:
            showinfo(title='Erro', message="Arquivo inválido")

    def select_file(self):
        filename = fd.askopenfilename(title='Selecione o arquivo', initialdir='/')
        return self.pp1.set(filename)

app()



