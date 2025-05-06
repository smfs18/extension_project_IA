import re #biblioteca que permite fazer remoção de elementos que não se deseja em um texto.
import numpy as np #importando a biblioteca de matemática, permite criar gráficos, matrizes...

caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUWXYZ0123456789 " #conjunto de caracteres: letras maiúsculas, minúsculas, números e espaços.
map = {c: i for i, c in enumerate(caracteres)} #atribui um número inteiro para cada caracter
desmap = {i: c for c, i in map.items()} #faz o processo inverso, para cada número inteiro, atribui uma caracter

#BASE_TESTEI
with open("base_testI.txt", "r", encoding = "utf-8") as file: #abri o arquivo, configura para o português.
    conteudo = file.read() #chamo uma variável e armazeno nela o valor lido.
    texto_limpo = re.sub(r"[^a-zA-Z0-9\s]", "", conteudo) #limpa o texto de caracteres especiais, acentuação...
    #print (texto_limpo) para printar na tela o texto limpo

vetor = [map[c] for c in texto_limpo if c in map] #vai pegar a os caracteres do texto, 1 por 1 e vai aplicar o map, atribuir um número inteiro.
matriz = np.array(vetor).reshape(-1, 20) #vai criar a matriz de várias linhas por 20 colunas.
matriz_convertida = ''.join([desmap[i] for i in vetor]) #processo inverte, converter os números em caracteres.
np.savetxt("matrizI.csv", matriz, delimiter=",", fmt="%d") #cria um documento .csv da matriz.

#BASE_TESTEII
with open("base_testII.txt", "r", encoding = "utf-8") as file: #abri o arquivo, configura para o português.
    conteudo = file.read() #chamo uma variável e armazeno nela o valor lido.
    texto_limpo = re.sub(r"[^a-zA-Z0-9\s]", "", conteudo) #limpa o texto de caracteres especiais, acentuação...
    #print (texto_limpo) para printar na tela o texto limpo

vetor = [map[c] for c in texto_limpo if c in map] #vai pegar a os caracteres do texto, 1 por 1 e vai aplicar o map, atribuir um número inteiro.
matriz = np.array(vetor).reshape(-1, 20) #vai criar a matriz de várias linhas por 20 colunas.
matriz_convertida = ''.join([desmap[i] for i in vetor]) #processo inverte, converter os números em caracteres.
np.savetxt("matrizII.csv", matriz, delimiter=",", fmt="%d") #cria um documento .csv da matriz.