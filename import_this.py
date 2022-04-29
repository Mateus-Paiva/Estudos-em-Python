#TRABALHANDO COM LISTAS

def main ():
    lista_compras = (['pão','açucar','leite'])
    print(f'\nEu adoro comer {lista_compras[0]}!\n')
    add_lista(lista_compras)
    remover(lista_compras)
    ordem_alfabtica(lista_compras)
    ordem_inversa(lista_compras)
    ordem02(lista_compras)
    reverso(lista_compras)
    qtd_lista(lista_compras)
    nav_lista(lista_compras)

def mod_lista (x):
    x [-1] = 'Tomate'
    print(f'\nO último item da lista foi alterado para "{x[-1]}".')

#Função x.append('hot-dog') adiciona 1 item no final da lista
def add_lista(x):
    x.append('manteiga')
    x.append('suco')
    x.append('molho')
    x.append('macarrão')
    x.append('feijão')

    print(f'Novos itens foram adicionados a lista, inluíndo o leite que havia sido removido.\n\n  Itens adicionados a Lista: {x[-1]}, {x[-2]}, {x[-3]}, {x[-4]}, {x[-5]}.')
    print(f'\n{x}')

#Função x.insert(0, 'banana') insere um item em uma posição específica da lista
def add02_lista(x):
    x.insert(0,'Bolo')
    print(f'\nAdicionamos também o {x[0]} no ínicio da lista.')
    print(x)

#Função del lista [0] deleta permanentemente o item da posição informada da lista
def deletar (x):
    del x [0]
    print(f'\nRemovemos um item da lista.\n{x} usando a funçao "del"')


#Removido um item especifico de uma lista e armazenando esse item a uma váriavel, dessa forma
#podemos acessar esses valores escluídos em algum momento. Podemos excluir tambem usando a função
#DEL, porém não conseguimos acessar esse item excluido depois, como a função pop nos permite.
def pope(x):
    print(x)
    pop_lista = x.pop()
    print(pop_lista)
    print(x)

def remover (x):
    rem_item = 'suco'
    x.remove(rem_item)
    print(f'\n  Removemos o "{rem_item}" da lista de compras.')
    print(f'\n{x}')

#A função .sort() altera permanentemente a posição dos itens da lista.
def ordem_alfabtica (x):
    x.sort()
    print(f'\n  Agora a lista está em ordem alfabética.\nLista: {x}\n')

def ordem_inversa (x):
    x.sort(reverse=True)
    print(f'  Agora a lista está na ordem inversa.\nLista: {x}\n')

#A função .sorted() altera momentaneamente a posição dos itens da lista.
def ordem02 (x):
    print(f'  Com a função "sorted()". \n{sorted(x)}')
    print(f'\n  Sem a função "sorted()", a lista volta para o formato original. \n{x}')

#A função .reverse() inverte permanentemente a posição dos itens da lista, ele ignora a posição alfabérica dos itens
#e toma como base a ordem cronológica que a lista foi criada, nesse caso a ultima fica em primeiro, podemos fazer uma
#segunda reversão para retornar a posição inicial.
def reverso (x):

    x.reverse()
    print(f'\n  Podemos usar a função ".reverse()", para inverter a posição dos itens na lista de forma permanente.\n{x}')

    x.reverse()
    print(f'\n  Usando novamente essa mesma função, podemos retornar a lista para a posição inicial.\n{x}')

#Função len() nos permite checar quantos itens temos na lista, a contagem começa no 1 e não no 0.
def qtd_lista (x):
    quantidade = len(x)
    print(f'\nA função "len()" nos permite verificar a quantidade de itens de uma lista, a nossa lista contém "{quantidade}" itens.\n')

#Utilizando o laço "for alimentos in lista" - print (alimentos), para cada alimento dentro de lista, print os alimentos
#Dessa forma ele nos mostra em sequencia todos os itens da lista
def nav_lista (x):
    print('Usando o laço "for" para trazer todos os itens da lista em sequência, conforme abaixo:\n')
    for alimentos in x:
        print(alimentos)

main()























