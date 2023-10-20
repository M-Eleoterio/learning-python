print("Hello, World! These are my Python notes! Feel free to explore and learn. Variable names, comments and replies are in Brazilian Portuguese, so maybe you'll need a translator or something like this. Have fun and good hacking!")
print("--------------------------------------------------")

# VARIAVEIS
# booleano
""" 
is_python = True
is_java = False """

# armazenando condições
""" 
ingressos = 50
compradores = 250
ingressos_suficientes = (ingressos >= compradores)
print (ingressos_suficientes) 
"""

# valores comuns
""" 
nome = "Rvsso"
idade = 17
peso = 59.9
print(nome, idade, peso)
"""

# inputs
""" 
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
peso = input("Digite seu peso: ")
print(nome, idade, peso)
print('--------------------------------------------------') 
"""

# conversão
""" 
nome_conv = nome
idade_conv = int(idade)
peso_conv = float(peso)
print(type(nome_conv), type(idade_conv), type(peso_conv))
print('--------------------------------------------------') 
"""

# operadores 

""" 
soma = 1 + 1
multiplicacao = 4 * 4
divisao = 30 / 3
pontencia = 7 ** 2

print("soma", soma)
print("multiplicação", multiplicacao)
print("divisão", divisao)
print("potência", pontencia)
print('--------------------------------------------------')
 """
# condicionais
""" 
print("CONDICIONAIS")

idade = int(input("Informe a sua idade: "))
permitido = False
if (idade >= 18):
    permitido = True
    print("Você está permitido a entrar")
else:
    permitido = False
    print("Você NÃO está permitido a entrar") 

"""
""" 
salario = float(input("Informe seu salário: "))
if salario <= 3000:
    print("Programador Junior")
elif salario > 3000 and salario <= 6000:
    print("Programador Pleno")
elif salario > 6000 and salario <=15000:
    print("Programador Senior")
else:
    print("Gerente de Projetos")
"""

# listas
""" 
lista = [1, 2, 3]

print(lista[0], lista[1], lista[2])yu

lista[0] = 23

print(lista[0], lista[1], lista[2])

lista.append('Hello')
lista.append('World')
lista.append('!')

print(lista[3], lista[4] + lista[5]) 
"""
    
# loops
# for
""" 
notas = []

for x in range(5):
    id_aluno = input("RM: ")
    nota_aluno = input("Nota do Aluno: ")
    resultado = [id_aluno, nota_aluno]
    notas.append(resultado)

print(notas)
print("Quantidade de notas: ", len(notas) )

for n in notas:
    id_aluno = n[0]
    nota = n[1]
    print("O RM", id_aluno, "tirou a nota", nota)
 """

#OU
""" 
counter = 1

while counter <= 5:
    id_aluno = input("RM: ")
    nota_aluno = input("Nota do Aluno: ")
    resultado = [id_aluno, nota_aluno]
    notas.append(resultado)
    counter += 1

for n in notas:
    id_aluno = n[0]
    nota = n[1]
    print("O RM", id_aluno, "tirou a nota", nota)
 """

# objects / dicts
""" 
player = {
    "nome": "Rvsso",
    "level": 1,
    "hp": 100,
    "exp": 0,
    "dano": 5,
}

npcs = [
    {"nome": "Monstro 1", "dano": 2, "hp": 50, "exp": 5 },
    {"nome": "Monstro 2", "dano": 5, "hp": 100, "exp": 10 },
    {"nome": "Monstro 3", "dano": 10, "hp": 150, "exp": 15 },
    {"nome": "Chefe", "dano": 25, "hp": 200, "exp": 20 },
]
 """

# funcoes

def Soma(n1, n2):
    return n1 + n2

while True:
    n1 = int(input("Numero 1:"))
    n2 = int(input("Numero 2:"))

    res = Soma(n1, n2)
    print(n1 , '+', n2, '=', res)