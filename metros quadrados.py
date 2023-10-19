import math
medida = float(input("digite quantos metros quadrados"))
litros = medida / 6
latas = math.ceil(litros / 18)
galoes = math.ceil(litros / 3.6)
preco_latas = latas * 80
preco_galoes = galoes * 25
combinacao = (litros // 18) * 80 + (math.ceil(((litros % 18)/ 3.6)) * 25)
print("O preco so com latas e:", preco_latas)
print("O preco so com galoes e:", preco_galoes)
print("O preco com a combinacao e:", combinacao)
