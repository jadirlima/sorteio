import pandas as pd
import random
from tkinter import *
from tkinter.constants import DISABLED, NORMAL
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

root = Tk()
bg = PhotoImage(file = "logo_a.png")
root.iconphoto(True, bg)



class app():
    def __init__(self):
        self.root = root
        self.bg = bg
        self.janela()
        root.mainloop()

    def janela(self):

        self.root.title("   Sorteador PMBV V2.1")
        self.root.configure(background='#87CEFA')
        self.root.geometry("800x600")
        self.frames_da_janela()
        # self.root.resizable(False, False)

    def frames_da_janela(self):

        back = Label(self.root)
        back.la = self.bg
        back['image'] = back.la
        back.place(relx=0.02, rely=0.05, relwidth=0.96, relheight=0.93)

        titulo = Label(self.root, text="Sorteio Prefeitura Municipal de Boa Vista",
                       fg="SteelBlue", bg='#dfe3ee', justify='center', font=("Arial", 12,'bold'))
        titulo.place(relx=0.15, rely=0.06, relwidth=0.7)

        open_button = Button(self.root, text='Localizar arquivo', bd=2, bg='#4682B4', fg='White',
                                   font=('verdana', 8, 'bold'), command=self.select_file)
        open_button.place(relx=0.45, rely=0.1, relwidth=0.15, relheight=0.05)
        self.pp1 = StringVar()
        self.pp1.set("super_herois.xlsx")
        self.pp1_entry = Entry(self.root, textvariable=self.pp1, justify='center', state=DISABLED)
        self.pp1_entry.place(relx=0.60, rely=0.1, relwidth=0.25, relheight=0.05)

        self.bt_sortear = Button(self.root, text="Sortear", bd=2, bg='#4682B4', fg='White',
                                 font=('verdana', 10, 'bold'), state=NORMAL, command=self.sortear)
        self.bt_sortear.place(relx=0.15, rely=0.1, relwidth=0.15, relheight=0.05)

        self.bt_resetar = Button(self.root, text="Resetar", bd=2, bg='#4682B4', fg='White',
                                 font=('verdana', 10, 'bold'), command=self.resetar)
        self.bt_resetar.place(relx=0.3, rely=0.1, relwidth=0.15, relheight=0.05)

        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=2)
        self.frame_2.place(relx=0.09, rely=0.87, relwidth=0.8, relheight=0.09)

        self.resultado = StringVar()
        self.resetar()
        self.resultado1 = Label(self.root, textvariable=self.resultado,
                                fg="Gold", bg='#778899', justify="left", font=("Arial",16,'bold'))
        self.resultado1.place(relx=0.15, rely=0.89, relwidth=0.7)




    def resetar(self):
        self.bt_sortear['state'] = NORMAL
        return self.resultado.set("-".center(150,'-'))

    def sortear(self):
        # sleep(1)
        arquivo = self.pp1.get()

        try:
            try:
                servidores = pd.read_excel(arquivo)
                lista_servidores = (servidores.iloc[:, 0])
                self.bt_sortear['state'] = DISABLED
                sortedo = lista_servidores[random.randrange(len(lista_servidores))]
                sortedo= str(sortedo)
                sortedo=" [ "+sortedo.upper()+" ] "
                return self.resultado.set(sortedo.center(150,'-'))
            except FileNotFoundError:
                showinfo(title='Mensagem de Erro', message="Não foi possível identificar o arquivo de dados")
        except ValueError as excecao:
            showinfo(title='Mensagem de Erro', message="Arquivo inválido")


    def select_file(self):
        filename = fd.askopenfilename(title='Selecione o arquivo', initialdir='/', filetypes=[("Excel files", "*.xlsx; *.xls")])
        return self.pp1.set(filename)

app()




