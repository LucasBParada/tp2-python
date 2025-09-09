from tkinter import *
tela = Tk()
tela.title("Cadastro de Clientes")
tela.configure(background='#1e3743')
tela.geometry("700x600")

tela.resizable(True, True)
tela.maxsize(width=800,height=700)
tela.minsize(width=500,height=300)

lbl_titulo = Label(tela,text="CADASTRO DE CLIENTES",
                   font="arial 20 bold italic",
                   fg="green", background='#1e3743').place(x=175,y=10)

lbl_nome = Label(tela,text="Digite seu nome:"
                 ,background='#1e3743',
                 font="arial 12 bold italic",
                 fg="white").place(x=20,y=100)

txt_nome = Entry(tela,width=70,borderwidth=5,fg="blue",bg="white")
txt_nome.place(x=155,y=100)

lbl_email = Label(tela,text="Digite seu e-mail:"
                 ,background='#1e3743',
                 font="arial 12 bold italic",
                 fg="white").place(x=20,y=150)

txt_email = Entry(tela,width=70,borderwidth=5,fg="blue",bg="white")
txt_email.place(x=155,y=150)

lbl_telefone = Label(tela,text="Digite seu telefone:"
                 ,background='#1e3743',
                 font="arial 12 bold italic",
                 fg="white").place(x=20,y=200)

txt_telefone = Entry(tela,width=70,borderwidth=5,fg="blue",bg="white")
txt_telefone.place(x=170,y=200)

lbl_endereco = Label(tela,text="Digite seu endereço:"
                 ,background='#1e3743',
                 font="arial 12 bold italic",
                 fg="white").place(x=20,y=250)

txt_endereco = Entry(tela,width=70,borderwidth=5,fg="blue",bg="white")
txt_endereco.place(x=178,y=250)

def meu_click():
    lbl_hello = Label(tela,text="Dados do Cliente \n" + txt_nome.get() + "\n" + txt_email.get() +
                     "\n" + txt_telefone.get() +"\n" + txt_endereco.get())
    lbl_hello.place(x=275,y=450)

btn_botao = Button(tela,text="CADASTRAR CLIENTE",
                   font="arial 12 bold italic",
                   background="aqua",
                   fg="black",
                   command=meu_click)
btn_botao.place(x=245,y=400)

tela.mainloop()


