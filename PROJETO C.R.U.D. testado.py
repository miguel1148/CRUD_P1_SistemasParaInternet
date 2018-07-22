#   C.R.U.D. P1 ALGORITIMOS E PROGRAMAÇÃO
#   Sistemas para internet
#   PROF. Rafael Marques

#Definição do projeto   sistema de gerenciamento de equipe de software

    
#ALUNO:
'''
MIGUEL DA SILVA RAMALHO

f1 = open('DBM.txt','a')#Arquivo onde será guardado a lista de dicionario
f2 = open('DBP.txt','a')#Arquico onde será guardado a lista de numeros codigos
from random import randint
'''


#Lista de membros
NOME = 'nome'
COD = 'codigo'
DATA_ent = 'data_entrada'
DATA_s = 'data_saida'
FUNCAO = 'funcao'

DBM = [{NOME : 'miguel', COD : 1234, DATA_s : '01/01/16', DATA_ent: '01/02/16', FUNCAO:'dev'}
    
    ]
#lista de projetos
DBP = [
    {NOME : 'CRUD', COD : 1234, DATA_s: '11/11/16',DATA_ent : '01/12/16', FUNCAO:''},
    {NOME : 'x', COD : 1235, DATA_s: '11/11/16',DATA_ent : '01/12/16', FUNCAO:''}

    ]

#######################################################################
'''
def salvar(nome):
    f = open('DBM.txt','w')
    for i in nome :
        f.write(str(i[DATA_ent]) + '\t')
        f.write(str(i[DATA_s]) + '\t')
        f.write(str(i[COD]) + '\t')
        f.write((i[NOME]) + '\t')
        f.write((i[FUNCAO]) + '\t')
    f.close()

def ler():
    f = open('DBM.txt','r')
    lista1 = []
    for linha in f:
        data_entrada,data_saida,codigo,nome,funcao = linha.strip().split('\t')
        prod = {}
        prod[NOME] = nome
        prod[FUNCAO] = funcao
        prod[COD] = int(codigo)
        prod[DATA_s] = data_saida
        prod[DATA_ent] = data_entrada
        
        

        lista1.append(prod)
    f.close()
    return lista1




'''









################################################
#funcao imprimir 1 membro do DBM
def imprimir_membro(p):
    print('-nome %-20s  *funcao %-15s *cod%-5d  *data_ent%-10s data_saida%-3s' % (p[NOME], p[FUNCAO], p[COD], p[DATA_ent], p[DATA_s]))

#funcao imprimir uma lista de membros ou projetos
def imprimir(D):
    for p in D:
        imprimir_membro(p)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#busca um membro pelo nome, que esteja dentro de um projeto (pelo nome) EX. CRUD
def buscaMembro(nome,code):
    for m in DBM:
        if m[NOME] == nome and m[COD] == code :
            return m
    return None

#buca um projeto pelo nome, e retorna ele
def buscaProjeto(nome):
    for p in DBP:
        if p[NOME] == nome:
            return p
    return None

#busca um projeto pelo codigo, e retorna ele
def busca_COD(codigo):
    for p in DBP:
        if p[COD] == codigo:
            return p
        return None

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#commando addM adiciona um membro
def cmd_addM():
    nomeProj = input("Digite nome do projeto:")
    proj = buscaProjeto(nomeProj)

    if proj :
        nome = input('Digite o nome do membro:')
        membro = buscaMembro(nome, proj[COD])
        if membro :
            print('Membro ja esta nesse projeto')
        else:
            novo = { }
            novo[NOME] = nome
            novo[COD] = proj[COD]
            novo[DATA_s] = ''
            novo[FUNCAO] = input('digite a nova funcao: ')
            from datetime import date
            novo[DATA_ent] = date.today().day, date.today().month, date.today().year
            DBM.append(novo)
            print('Adictionado(a)')
    else:
        print('Projeto nao existe')

    


    
def imprimir_proj(proj):
    print(proj[NOME],'\nCodigo',proj[COD],'\nData de inicio',proj[DATA_ent],'\nData de entrega',proj[DATA_s])  
       

#comando addP
def cmd_addP():
    nome = input('Digite o nome do projeto:')
    proj = buscaProjeto(nome)
    if proj :
        print('Esse nome já esta registrado no sistema')
        imprimir_proj(proj)
        
    else:
        novo = { }
        novo[COD]= int(input('digite o codigo de 4 digitos: '))
        for x in DBP:
            if x[COD] ==novo[COD]:
                print('Esse codigo já esta registrado no sistema')
                break
        else:
            novo[NOME] = nome
            novo[DATA_s] = input('Digite o prazo para entrega:')
            novo[FUNCAO] = input('digite a finalidade do projeto: ')
            from datetime import date
            novo[DATA_ent] = date.today().day, date.today().month, date.today().year
            DBP.append(novo)
            print('Adictionado(a)')
            
        

#comando listM 
def cmd_listM():
    imprimir(DBM)


#comando updateM  ** atualiza a funcao de um membro ja existente do grupo **
def cmd_updateM():
    nome = input('Digite o nome: ')
    codigo = int(input('digite o codigo: '))
    for x in DBM:
        if x[NOME] == nome:
            if x[COD] == codigo:
                x[FUNCAO] = input('digite a nova funcao: ')
                print('Membro Atualizado')
                break
    else:
        print('Membro ou Codigo invalidos\nTente novamente')
        
# comando del_M   *Deletar um membro do grupo*        
def cmd_delM():
    nome = input('Digite o nome do membro: ')
    codigo = int(input('digite o codigo: '))
    for x in DBM:
        if x[NOME] == nome:
            if x[COD] == codigo:
                from datetime import date
                x[DATA_s] =str('saida'), date.today().day, date.today().month, date.today().year
                break
    else:
        print('Membro ou Codigo invalidos\nTente novamente')
                
#COMANDO updateP ** atualiza um projeto dando a ele uma nova funcao **
def cmd_updateP():
    nome = input('Digite o nome do projeto: ')
    for x in DBP:
        if x[NOME] == nome:
            x[FUNCAO] = input('digite uma nova Finalidade : ')
            x[DATA_s] = input('digite um novo prazo p/ entrega : ')
            print('Projeto Atualizado')
            break
    else:
        print('Membro ou Codigo invalidos\nTente novamente')
        
#OBS. comando del_P ainda em fase de acabamento         
def cmd_delP():
    nome = input('Digite o nome: ')
    codigo = int(input('digite o codigo: '))
    for x in DBP:
        if x[NOME] == nome:
                del x
                break
    else:
        print('Membro ou Codigo invalidos\nTente novamente')

#comando listP Imprimi a lista de projetos registrados no banco
def cmd_listP():
    imprimir(DBP)



#menu com todos os comandos pro usuário ver o que pode ser digitado
def menu():
    print('Comandos:')
    print('\t1 - imprime todos os membros do projeto')
    print('\t2 - adiciona novo membro')
    print('\t3 - atualiza função de um membro')
    print('\t4 - imprime todos os projetos')
    print('\t5 - adiciona novo projeto')
    print('\t6 - atualiza dados de um projeto')
    print('\t7 - excluir membro do grupo')
    print('\tExit - sai da aplicação')

'***************************************************************************************'
#MAIN DO PROJETO CRUD
'***************************************************************************************'
menu() #chama o menu pra imprimir na primeira vez
while True:

    cmd = input(":").lower()
    
    if cmd == '1':	#print = imprime todos os membros
        cmd_listM()

    elif cmd == '2':	#add = adicionar um novo elemento
        cmd_addM()
    elif cmd == '3': #update = atualizar um elemento existente
        cmd_updateM()
    elif cmd == '4':    #print = imprime todos os membros
        cmd_listP()
    elif cmd == '5':	#add = adicionar um novo elemento
        cmd_addP()
    elif cmd == '6': #update = atualizar um elemento existente
        cmd_updateP()
    elif cmd == '7': #exclui um membro do grupo
        cmd_delM()
    elif cmd == 'exit':	#exit = sair do programa
        print('fim')
        break
    
    else:
        menu()
    

        
    
