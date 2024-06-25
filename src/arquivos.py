import os
from datetime import datetime

def leituraArquivo(vetor, nomeArquivo):
    with open(nomeArquivo, 'r') as file:
        linhasArquivo = file.readlines()
        linhaNumeros = linhasArquivo[-1].strip()

    for numero in linhaNumeros.split(", "):
        vetor.append(int(numero))

def escritaArquivo(nomeArquivo, tabelaSaida):
    dataFormatada = datetime.now().strftime("%d-%m-%Y-%H:%M:%S")
    nomeArquivo += '-' + dataFormatada + '.csv'

    conteudo = f"Data e Hora de Geração: {dataFormatada}\nTempos em segundos:\n{tabelaSaida}"

    with open(nomeArquivo, 'w') as file:
        file.write(conteudo)
