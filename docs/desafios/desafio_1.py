# desafio 1
import json
from datetime import datetime, timedelta
from collections import Counter
"""PRODUTOS = [
    {"nome": "Notebook Gamer", "categoria": "Eletrônicos", "avaliação": 4.5},
    {"nome": "Geladeira", "categoria": "Eletrodomésticos", "avaliação": 4.7},
    {"nome": "Smartphone", "categoria": "Eletrônicos", "avaliação": 4.9},
    {"nome": "Liquidificador", "categoria": "Eletrodomésticos", "avaliação": 4.3},
    {"nome": "Fone de Ouvido", "categoria": "Eletrônicos", "avaliação": 4.8},
]

def consultar_produtos(categoria) :

    produtos = sorted(PRODUTOS, key=lambda d: d['avaliação'], reverse=True)
    found = [item for item in produtos if item['categoria'] == categoria]
    return found 

found = consultar_produtos("Eletrônicos")
print (json.dumps(found, indent=2))"""


# desafio 2 

"""agenda = []

def adicionar_contato (nome, telefone, email) : 
    global agenda
    novo_contato = {
        "nome" : nome,
        "telefone" : telefone,
        "email" :  email
    }
    agenda.append(novo_contato)
    #return agenda

contato = adicionar_contato ("Alice", "1234-5678", "alice@example.com")
contato = adicionar_contato("Bob", "9876-5432", "bob@example.com")
print ("novos clientes :: ", agenda)

def buscar_contato (nome) :
    global agenda
    contato_found = [item for item in agenda if item['nome'] == nome]
    return contato_found

nome_find = "Alice"
contato = buscar_contato(nome_find)
if len(contato) > 0 : 
    print ("cliente pesquisado e encontrato:: ",contato)
else : 
    print ("Nenhum registro encontrado para :: ", nome_find)

def remover_contato (nome) :
    global agenda
    init = len(agenda)
    agenda = [item for item in agenda if item['nome'] != nome]
    end = len(agenda)
    if end < init : 
        return True
    else :
        return False        

if remover_contato("Bob") :
    print ("Bob removido com sucesso :: ", agenda)
else :
    print ("Bob não encontrato ou algum problema aconteceu :: ", agenda)"""

# desafio 3

"""livro = []

def cadastrar_livro (titulo, autor, ano, status) : 
    global livro 
    unidade = {"titulo":titulo,"autor":autor,"ano":ano,"status":status,"leitor":None}
    init = len(livro)
    cadastrar = livro.append(unidade)
    end = len(livro)
    if end > init :
        return True
    return False

cadastrar = cadastrar_livro("Dom Casmurro", "Machado de Assis", 1899,"Disponivel")
if cadastrar :
    print ("Livro cadastrado com sucesso")
else :
    print ("Livro não cadastrado")
cadastrar = cadastrar_livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943,"Disponivel")
if cadastrar :
    print ("Livro cadastrado com sucesso")
else :
    print ("Livro não cadastrado")

def emprestar_livro (titulo,leitor) :
    global livro
    emprestar = [k for k, item in enumerate(livro) if item['titulo'] == titulo and item['status'] == "Disponivel"]
    if len(emprestar) > 0 :
        livro[emprestar[0]]['status'] = "Emprestado"
        livro[emprestar[0]]['leitor'] = leitor
        return True    
    return False

print ("pegando emprestado")
emprestar = emprestar_livro("Dom Casmurro","Aline")
if emprestar :
    print ("Livro alugado com sucesso")
else :
    print ("Livro indisponivel para aluguel")

def devolver_livro (titulo) :
    global livro
    emprestar = [k for k, item in enumerate(livro) if item['titulo'] == titulo]
    if len(emprestar) > 0 :
         livro[emprestar[0]]['status'] = "Disponivel"
         livro[emprestar[0]]['leitor'] = None
         return True    
    return False

print ("devolvendo livros")
devolver = devolver_livro("Dom Casmurro")
if devolver :
    print ("Livro devolvido com sucesso")
else :
    print ("Falha na devolução")

def consultar_livros() : 
    return livro

livros = consultar_livros()
print ("consultando livros :: ",json.dumps(livros))"""

# desafio Sistema de Análise de Logs

# logs 
logs = [
    {"data": "2024-02-20 08:30:00", "usuario": "alice", "acao": "login", "status": "sucesso"},
    {"data": "2024-02-20 09:00:00", "usuario": "bob", "acao": "login", "status": "falha"},
    {"data": "2024-02-20 09:30:00", "usuario": "alice", "acao": "acesso", "status": "sucesso"},
    {"data": "2024-02-20 10:00:00", "usuario": "carol", "acao": "logout", "status": "sucesso"},
    {"data": "2024-02-21 11:00:00", "usuario": "alice", "acao": "logout", "status": "sucesso"},
    {"data": "2024-02-22 12:30:00", "usuario": "bob", "acao": "acesso", "status": "falha"},
]

#carregar logs 
def carregar_logs(log):
    global logs
    len_init = len(logs)
    logs = logs + log
    len_end = len(logs)
    if len_end > len_init : 
        return True
    return False

print ("adicionando novos logs")
log = [
    {"data": "2024-03-01 08:30:00", "usuario": "alice", "acao": "login", "status": "sucesso"},
    {"data": "2024-03-01 09:00:00", "usuario": "bob", "acao": "login", "status": "falha"},
    {"data": "2024-03-01 09:30:00", "usuario": "alice", "acao": "acesso", "status": "sucesso"},
    
    {"data": "2024-03-03 16:51:01", "usuario": "alice", "acao": "login", "status": "falha"},
    {"data": "2024-03-03 16:53:10", "usuario": "alice", "acao": "login", "status": "falha"},
    {"data": "2024-03-03 16:59:20", "usuario": "alice", "acao": "login", "status": "falha"},

    {"data": "2024-03-03 16:53:00", "usuario": "bob", "acao": "login", "status": "falha"},
    {"data": "2024-03-03 16:58:01", "usuario": "bob", "acao": "login", "status": "falha"},
    {"data": "2024-03-03 16:58:15", "usuario": "bob", "acao": "login", "status": "falha"},
    {"data": "2024-03-03 16:58:45", "usuario": "bob", "acao": "login", "status": "falha"},

    {"data": "2024-03-05 09:51:01", "usuario": "alice", "acao": "login", "status": "falha"},
    {"data": "2024-03-05 09:53:10", "usuario": "alice", "acao": "login", "status": "falha"},
    {"data": "2024-03-05 09:59:20", "usuario": "alice", "acao": "login", "status": "falha"},

    {"data": "2024-03-05 09:53:00", "usuario": "bob", "acao": "login", "status": "falha"},
    {"data": "2024-03-05 09:58:01", "usuario": "bob", "acao": "login", "status": "falha"},
    {"data": "2024-03-05 09:58:15", "usuario": "bob", "acao": "login", "status": "falha"},
    {"data": "2024-03-05 09:58:45", "usuario": "bob", "acao": "login", "status": "falha"},
    
]
carregar_logs(log)
print ("novos logs",logs)

# analisar acoes por usuario
def acoes_por_usuario(usuario):
    global logs    
    acoes = [item for item in logs if item['usuario'] == usuario]
    if len(acoes) > 0 :
        acoes = sorted(acoes, key = lambda d: d['data'])
        return acoes
    return []

print ("check acoes por usuarui")
acoes_usuario = acoes_por_usuario("bob")
print ("acoes por usuarios")
print (acoes_usuario)

# contabilizar acoes de sucesso e falha
def acontabilizar_acoes(status):
    global logs    
    count = sum(1 for item in logs if item['status'] == status)
    return count 

print ("check acontabilizar_acoes")
count_by_status = acontabilizar_acoes("sucesso")
print ("count_by_status sucesso",count_by_status)
count_by_status = acontabilizar_acoes("falha")
print ("count_by_status falha",count_by_status)

# filtrar logs por data 
def filtrar_logs_por_data (data_inicial,data_final):
    global logs
    data_inicial = datetime.strptime(data_inicial,"%Y-%m-%d %H:%M:%S")
    data_final = datetime.strptime(data_final,"%Y-%m-%d %H:%M:%S")
    filtro_logs = list(filter(lambda log: data_inicial <= datetime.strptime(log['data'],"%Y-%m-%d %H:%M:%S") <= data_final,logs))
    return filtro_logs

print ("check filtrar_logs_por_data")
data_inicio = "2024-02-01 00:00:00" 
data_fim = "2024-02-28 23:59:59"
filtros_logs_por_data = filtrar_logs_por_data(data_inicio,data_fim)

# envia alerta via sms ou database
def send_alert (user,msg):
    # função para enviar msg de alerta
    send (user,msg)

# detect anomalia 
def detectar_comportamente_suspeito ():
    global logs
    data_hora_atual = datetime.now()
    um_minuto = timedelta(minutes=60)
    data_hora_menos_1_min = data_hora_atual - um_minuto
    log_ultimos_60_min = list(
            filter(
                lambda log: 
                    data_hora_menos_1_min <= datetime.strptime(log['data'],"%Y-%m-%d %H:%M:%S")<=data_hora_atual 
                    and log['status'] == 'falha' 
                    and log['acao'] == 'login',logs)
                    )

    por_usuario = [item['usuario'] for item in log_ultimos_60_min]
    logs_de_atencao = Counter(por_usuario)
    if len(logs_de_atencao) > 1 : 
        for item,value in logs_de_atencao.items() :
            if value > 2 :
                # função hipotetica para enviar , alerta ou email
                send_alert(item,"Compartamento estranho em login")

print ("check compartamento estranho log")
detectar_comportamente_suspeito()

def relatorio_por_usuario (data_inicio, data_fim) : 
    global logs
    data_inicio = datetime.strptime(data_inicio,"%Y-%m-%d %H:%M:%S")
    data_fim = datetime.strptime(data_fim,"%Y-%m-%d %H:%M:%S")
    filtro = list(filter(lambda log: data_inicio <= datetime.strptime(log['data'],"%Y-%m-%d %H:%M:%S")<=data_fim,logs))
    registros = [(log['usuario'],log['acao'],log['status']) for log in filtro]
    registros = Counter(registros)
    return registros

data_inicio = "2024-01-01 00:00:00"
data_fim = "2024-03-31 23:59:59"
relatorio = relatorio_por_usuario(data_inicio,data_fim)
print ("relatorio :: ",relatorio)