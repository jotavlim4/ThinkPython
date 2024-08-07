# 1. volume de uma esfera de raio 5.
r = 5
pi = 3.14
vol_esf = (4/3)*pi*(r**3)
print('o volume de uma esfera de raio 5 é', vol_esf)

# 2. custo da produção de capas de livro.
quantitade = 60

preco_capa = 24.95
desconto = .4
preco_capa = preco_capa*(1 - desconto)

trans_primeiro = 3.0
trans_demais = .75
transporte = (quantitade - 1) * trans_demais + trans_primeiro

custo_total = preco_capa*quantitade + transporte

print('o custo total para o pedido de 60 copias é', custo_total)

# corrida matinal:
tempo_inicial = 6*3600 + 52*60 # tempo em segundos

tempo_p1 = 8*60 + 15
tempo_p2 = 7*60 + 12

tempo_corrida = 3*tempo_p2 + 2*tempo_p1
tempo_final = tempo_inicial + tempo_corrida

print(tempo_final)

horas = tempo_final//3600
minutos = (tempo_final%3600)//60
segundos =(tempo_final%3600)%60

print(f'chega em casa as {horas}h {minutos}min {segundos}s')
