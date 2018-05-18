from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

##Interface Grafica em TKINTER Criada By criada por todo mundo 1º Periodo FACOL##

######Banco de Dados######

def banco():
    global conn, cursor
    conn = sqlite3.connect('moreno.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, endereco TEXT, telefone TEXT, cpf TEXT UNIQUE, plano TEXT)")

######Funções do Banco de Dados######

def cadastro():
    if Var.get() == '' or caixa_cliente.get() == '' or caixa_endereco == '' or caixa_endereco == '' or caixa_cpf == '':
        messagebox.showinfo('MorenoNet', 'Informe seus Dados e Escolha o Plano!')
    else:
        banco()
        nome = caixa_cliente.get()
        endereco = caixa_endereco.get()
        telefone = caixa_contato.get()
        cpf = caixa_cpf.get()
        plano = Var.get()
        cursor.execute('''INSERT INTO clientes (nome, endereco, telefone, cpf, plano) VALUES (?, ?, ?, ?, ?)''', (nome, endereco, telefone, cpf, plano))
        conn.commit()
        messagebox.showinfo('MorenoNet', 'Cliente Cadastrado com Sucesso!')

def clientes():
    banco()
    clientes.delete(*clientes.get_children())
    lista = cursor.execute('SELECT * FROM clientes')
    for data in lista:
        clientes.insert('', END, values=(data))
    messagebox._show('MorenoNet', 'Dados Carregados e Atualizados!')

def atualizar():
    banco()
    novo_Plano = Var.get()
    for selecao_UPD in clientes.selection():
        conn.execute('''UPDATE clientes SET plano=? WHERE ID =?''', (novo_Plano, clientes.set(selecao_UPD, '#1')))
        conn.commit()
        conn.close()
        messagebox.showinfo('MorenoNet', 'Plano Atualizado: Por Favor Atualize em Clientes!')

def deletar():
    banco()
    for selecao in clientes.selection():
        conn.execute('''DELETE FROM clientes WHERE id=?''', (clientes.set(selecao, '#1')))
        conn.commit()
        clientes.delete(selecao)
        conn.close()

def Search():
    if procurarvar.get() != "":
        clientes.delete(*clientes.get_children())
        conn = sqlite3.connect("moreno.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM 'clientes' WHERE `nome` LIKE ? OR `cpf` LIKE ?", ('%'+str(procurarvar.get())+'%', '%'+str(procurarvar.get())+'%'))
        fetch = cursor.fetchall()
        for data in fetch:
            clientes.insert('', 'end', values=(data))
        cursor.close()
        conn.close()        
######Toda Inteface Gráfica######

app = Tk()

######Variaveis######

Var = StringVar()
procurarvar = StringVar()


######Configuração da Janela principal######

app.title('MORENO NET')
app.geometry('836x500')
app.configure(bg='red')
app.wm_resizable(width=0, height=0)

######Frames######

top = Frame(app, width=836, height=60, bd=1, bg='red', relief='raise')
top.pack(side=TOP)
L = Frame(app, width=430, height=500, bd=1, bg='red', relief='raise')
L.pack(side=LEFT)
L2 = Frame(L, width=15, height=313, bd=1, bg='white', relief='raise')
L2.place(x=250, y=125)
R = Frame(app, width=430, height=500, bd=1, bg='red', relief='raise')
R.pack(side=RIGHT)

#######labels######

label1 = Label(top, text="SISTEMA DE CRUD PYTHON", fg='black', bg='red', font=('arial', 16))
label1.place(x=290, y=16)
nome_busca = Label(L, text='Nome do Cliente', fg='black', bg='red', font=('arial', 12))
nome_busca.place(x=10, y=40)
nome_cliente = Label(L, text='Nome', fg='black', bg='red', font=('arial', 12))
nome_cliente.place(x=10, y=100)
endereco_ = Label(L, text='Endereço', fg='black', bg='red', font=('arial', 12))
endereco_.place(x=10, y=165)
numero_contato = Label(L, text='Número de Contato', fg='black', bg='red', font=('arial', 12))
numero_contato.place(x=10, y=230)
cpf_ = Label(L, text='CPF', fg='black', bg='red', font=('arial', 12))
cpf_.place(x=10, y=295)
plano_ = Label(L, text='Selecione o Plano', fg='black', bg='red', font=('arial', 12))
plano_.place(x=280, y=120)

######Caixa de Entrada######

caixa_busca = Entry(L, width=15, font=('arial', 14), textvariable=procurarvar)
caixa_busca.place(x=140, y=40)
caixa_cliente = Entry(L, width=20, font=('arial', 14))
caixa_cliente.place(x=10, y=125)
caixa_endereco = Entry(L, width=20, font=('arial',14))
caixa_endereco.place(x= 10, y=190)
caixa_contato = Entry(L, width=20, font=('arial', 14))
caixa_contato.place(x=10, y=255)
caixa_cpf = Entry(L, width=20, font=('arial', 14))
caixa_cpf.place(x=10, y=320)

######Botões######

b_busca = Button(L, text='Buscar', bg='gray',command=Search, fg='white', font=('arial', 11))
b_busca.place(x=320, y=37.8)
b_cadastrar = Button(L, width=18, text='Cadastrar', command=cadastro, fg='white', bg='gray', font=('arial', 16))
b_cadastrar.place(x=10, y=380)
b_clientes = Button(L, width=10, text='Clientes', command=clientes, fg='white', bg='gray', font=('arial', 11))
b_clientes.place(x=320, y=320)
b_delete = Button(L, width=10, text='Deletar', command=deletar, bg='gray', fg='white', font=('arial',11))
b_delete.place(x=320, y=391)
b_atualizar = Button(L, width=10, text='Atualizar', command=atualizar, bg='gray', fg='white', font=('arial', 11))
b_atualizar.place(x=320, y=355)

######CheckButton######

quinze_mb = Radiobutton(L, text='15 MB', variable=Var, value='15MB', fg='black', bg='red', font=('arial', 14))
quinze_mb.place(x=280, y=150)
cinquenta_mb = Radiobutton(L, text='50 MB', variable=Var, value='50MB', fg='black', bg='red', font=('arial', 14))
cinquenta_mb.place(x=280, y=190)
cem_mb = Radiobutton(L, text='100 MB', variable=Var, value='100MB', fg='black', bg='red', font=('arial', 14))
cem_mb.place(x=280, y=230)
quientos_mb = Radiobutton(L, text='500 MB', variable=Var, value='500MB', fg='black', bg='red', font=('arial', 14))
quientos_mb.place(x=280, y=270)

######Treeview######

scrollbary = Scrollbar(R, orient=VERTICAL)
scrollbarx = Scrollbar(R, orient=HORIZONTAL)
clientes = ttk.Treeview(R, columns=('ID', 'Nome', 'Endereço', 'Telefone', 'CPF', 'Plano'), selectmode='extended', height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=clientes.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=clientes.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
clientes.heading('ID', text='ID', anchor=CENTER)
clientes.heading('Nome', text='Nome', anchor=CENTER)
clientes.heading('Endereço', text='Endereço', anchor=CENTER)
clientes.heading('Telefone', text='Telefone', anchor=CENTER)
clientes.heading('CPF', text='CPF', anchor=CENTER)
clientes.heading('Plano', text='Plano', anchor=CENTER)
clientes.column('#0', stretch=NO, minwidth=0, width=0, anchor=CENTER)
clientes.column('#1', stretch=NO, minwidth=0, width=100, anchor=CENTER)
clientes.column('#2', stretch=NO, minwidth=0, width=100, anchor=CENTER)
clientes.column('#3', stretch=NO, minwidth=0, width=100, anchor=CENTER)
clientes.column('#4', stretch=NO, minwidth=0, width=100, anchor=CENTER)
clientes.column('#5', stretch=NO, minwidth=0, width=100, anchor=CENTER)
clientes.column('#6', stretch=NO, minwidth=0, width=100, anchor=CENTER)
clientes.pack()

app.mainloop()
