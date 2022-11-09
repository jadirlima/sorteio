from tkinter import *
from tkinter import ttk
root=Tk()
class app():
    def __init__(self):
        self.root = root
        self.janela()
        self.frames_da_janela()
        self.widgets_frame1()
        root.mainloop()
    def janela(self):
        self.root.title("Pontos Percentuais para Percentagem e vice-versa")
        self.root.configure(background='#1e3743')
        self.root.geometry("500x400")
        self.root.resizable(False, False)
    def frames_da_janela(self):
        self.frame_1 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=2)
        self.frame_1.place(relx=0.02, rely=0.05, relwidth=0.96, relheight=0.9)
    def widgets_frame1(self):
        self.abas = ttk.Notebook(self.frame_1)
        self.pppercentagem = Frame(self.abas)
        self.percentagemppp = Frame(self.abas)
        self.pppercentagem.configure(background="#dfe3ee")
        self.percentagemppp.configure(background="#dfe3ee")
        self.abas.add(self.pppercentagem, text="Pontos Percentuais para Percentagem")
        self.abas.add(self.percentagemppp, text="Percentagem para Pontos Percentuais ")
        self.abas.place(relx=0, rely=0, relwidth=0.98, relheight=0.98)

        self.pp1 = IntVar()
        self.lb_pp1 = Label(self.pppercentagem, text="Pontos Percentuais",bg='#dfe3ee', fg='#107db2')
        self.lb_pp1.place(relx=0.2, rely=0.2)
        self.pp1_entry = Entry(self.pppercentagem, textvariable=self.pp1,justify='center')
        self.pp1_entry.place(relx=0.6, rely=0.2, relwidth=0.3)

        self.bt_calcular1 = Button(self.pppercentagem, text="Calcular", bd=2,bg='#107db2', fg='white',
                                   font=('verdana', 12, 'bold'),command=self.butaoclick1)

        self.bt_calcular1.place(relx=0.35, rely=0.4, relwidth=0.35, relheight=0.1)
        self.resultado = StringVar()
        self.resultado1 = Label(self.pppercentagem, textvariable=self.resultado,
                                fg="blue",bg='#dfe3ee',justify='center',font=("Arial"))
        self.resultado1.place(relx=0.15, rely=0.6, relwidth=0.7)

        # Percentagem para Pontos Percentuais
        self.percentagem1 = DoubleVar()
        self.lb_percentagem1 = Label(self.percentagemppp, text=" Percentagem  ",bg='#dfe3ee', fg='#107db2')
        self.lb_percentagem1.place(relx=0.2, rely=0.2)
        self.percentagem1_entry = Entry(self.percentagemppp, textvariable=self.percentagem1,justify='center')
        self.percentagem1_entry.place(relx=0.6, rely=0.2, relwidth=0.3)
        # Butão de Calcular
        self.bt_calcular2 = Button(self.percentagemppp,text="Calcular", bd=2,bg='#107db2',
                                   fg='white', font=('verdana', 8, 'bold'),command=self.butaoclick2)
        self.bt_calcular2.place(relx=0.35, rely=0.4, relwidth=0.35, relheight=0.1)
        self.resultado1 = StringVar()
        self.finalresultado2 = Label(self.percentagemppp, textvariable=self.resultado1,fg="blue",
                                     bg='#dfe3ee',justify='center',font=("Arial"))
        self.finalresultado2.place(relx=0.15, rely=0.6, relwidth=0.7)

    def butaoclick1(self):
        a = self.pp1.get()
        percentagem = (1*a)/100
        mensagem = f"{a} pontos percentuais são {percentagem} %"
        return self.resultado.set(mensagem)

    def butaoclick2(self):
        b = self.percentagem1.get()
        pontospercentuais = b*100
        mensagem = f"{b} % são {pontospercentuais} pontos percentuais "
        return self.resultado1.set(mensagem)
app()