tamanhoArquivo = float(input("digite o tamanho do arquivo para download: "))
velocidade = float(input("digite a velocidade de um link de internet: "))
segundos = tamanhoArquivo/velocidade
minutos = int(segundos/60)
segundos = segundos%60
print("Tempo aproximado para download: " +
str(minutos) + "minutos e " + str(segundos) + "segundos")
