def print_twice(value):
    print(value)
    print(value)
    #print(cat)

def cat_twice(line1, line2):
    cat = line1 + line2
    print_twice(cat)

# 'cat' só existe dentro de 'cat_twice', pois são variáveis locais.
# assim como 'line1' e 'line2'
# logo podemos usar esses mesmos nomes se necessário sem ter nenhum de problema.
# variáveis locais definidas dentro de funcoes e os próprios parametros só existem
# enquanto as instrucoes da funcao onde foram definidas estão sendo executadas.

line1 = 'Joao Victor '
line2 = 'é legal!'

cat_twice(line1, line2)
