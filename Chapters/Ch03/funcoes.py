# def é usado para definir novas funcoes.
# obrigatoriamente precisamos de um nome para ela, esse nome deve respeitar as mesmas regras
# para nomes de variáveis.
# após o nome temos obrigatoriamente (), esses parenteses recebem os parametros e em seguida tempos :
# tudo após isso é o corpo da funcao, ele deve estar identeado.
def print_lyrics(): #cabeçalho da funcao
    #corpo da funcao
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

# print_lyrics() # chamaos a funcao usando seu cabeçalho

# a definição da funcao deve vir antes da chamada.
# chamar uma funcao que é definida posteriormente gerará um erro.
# repeat_lyrics()

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()

# apenas definir a funcao não faz com que ela seja executada,
# precisamos invocar/chamar ela para que as intrucoes em seu corpo
# produza algum efeito.
