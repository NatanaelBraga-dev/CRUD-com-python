'''Crud com tkinter e pymysql'''

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql.cursors

'''criação da conexão com banco de dados'''
conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='crud_alunos',
    cursorclass=pymysql.cursors.DictCursor
)

'''funções do CRUD'''
def adicionar():
    nome = txt_nome.get()
    idade = int(txt_idade.get())
    cursos = combobox.get()

    sql = "INSERT INTO alunos (nome,idade,cursos) values(%s, %s, %s)"
    cursor = conexao.cursor()
    cursor.execute(sql,(nome,idade,cursos))
    conexao.commit()
    messagebox.showinfo("","você foi registrado com sucesso")

def excluir():
    matricula = txt_matricula.get()
    sql = "DELETE FROM alunos WHERE matricula=%s"
    cursor = conexao.cursor()
    cursor.execute(sql,(matricula))
    conexao.commit()
    messagebox.showinfo("","registro excluido com sucesso")

def editar():
    matricula = txt_matricula.get()
    nome = txt_nome.get()
    idade = txt_idade.get()
    cursos = combobox.get()

    sql = "UPDATE alunos SET nome=%s, idade=%s, cursos=%s WHERE matricula=%s"
    cursor = conexao.cursor()
    cursor.execute(sql,(nome,idade,cursos,matricula))
    conexao.commit()
    messagebox.showinfo("","registro editado com sucesso")


'''começo da interface com tkinter'''
janela = Tk()

'''criação da janela do tkinter'''

janela.title("crud de usuários")
janela.geometry('600x600')

'''criação do campo de matricula'''
label_matricula = Label(text='Digite a matricula:', fg='black', font=12)
label_matricula.grid(column=0,row=0)

txt_matricula = Entry(janela,font=11, fg='black')
txt_matricula.grid(column=1,row=0)

'''criação do campo nome'''
label_nome = Label(text='Digite seu nome:',fg='black',font=12)
label_nome.grid(column=0,row=1)

txt_nome = Entry(janela,fg='black',font=11)
txt_nome.grid(column=1,row=1)

'''criação do campo idade'''
label_idade = Label(text='Digite sua idade:',font=12,fg='black')
label_idade.grid(column=0,row=2)

txt_idade = Entry(janela,fg='black',font=11)
txt_idade.grid(column=1,row=2)

'''criação do combobox de cursos'''
label_cursos = Label(text='Escolha seu curso',font=12,fg='black')
label_cursos.grid(column=0,row=3)

lista = ['Adiministração','Desenvolvimento de sistemas','Eletrotécnica','Mecânica']

combobox = ttk.Combobox(janela,values=lista)
combobox.grid(column=1,row=3)

'''criação dos botões'''
botao_adicionar = Button(bg='yellowgreen',fg='black',text='Adicionar',command=adicionar)
botao_adicionar.grid(column=0,row=5)

botao_editar = Button(bg='yellow',fg='black',text='Editar', command=editar)
botao_editar.grid(column=1,row=5)

botao_excluir = Button(fg='black',bg='red',text='Excluir', command=excluir)
botao_excluir.grid(column=2,row=5)

lista_de_dados = Listbox(janela,width=50)
lista_de_dados.grid(column=1,row=6)

'''função de listar os alunos registrados'''
def listar():
    sql = "SELECT * FROM alunos"
    cursor = conexao.cursor()
    cursor.execute(sql)
    tb_dados = cursor.fetchall()
    for item in tb_dados:
        lista_de_dados.insert(END,item)

listar()

janela.mainloop()