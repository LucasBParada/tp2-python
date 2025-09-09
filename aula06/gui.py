from tkinter import *
tela = Tk()
tela.title("Fatec Registro")
tela.configure(background='#1e3743')
tela.geometry("700x600")

tela.resizable(True, True)
tela.maxsize(width=800,height=700)
tela.minsize(width=500,height=300)

lbl_teste = Label(tela,text="TESTE").place (x=10, y=10)
lbl_nome = Label(tela, text="Nome").place (x=10, y=30)
lbl_cpf = Label(tela, text="CPF").place (x=10, y=50)


tela.mainloop()