from datetime import datetime
from arquivos import leituraArquivo

def calcularTabelaSaidaRadix(tamanhos, tabelaSaida):
    ordens = ["Aleatorio", "Crescente", "Decrescente"]
    tipos = ["", "-RangeMenor", "-RangeMaior", "-CEP", "-Iguais", "-Extremo"]
    nomeArquivo = ""

    tabelaSaida += ("Tamanho/Tipo,Aleatorio,Aleatorio-RangeMenor,Aleatorio-RangeMaior,Aleatorio-CEP,Aleatorio-Iguais,Aleatorio-Extremo,Crescente,Crescente-RangeMenor,Crescente-RangeMaior,Crescente-CEP,Crescente-Iguais,Crescente-Extremo,Decrescente,Decrescente-RangeMenor,Decrescente-RangeMaior,Decrescente-CEP,Decrescente-Iguais,Decrescente-Extremo\n")
    tempoTotal = 0.0

    for tamanho in tamanhos:
        tabelaSaida += (f"{tamanho},")

        for ordem in ordens:
            for tipo in tipos:
                nomeArquivo = f"datasets/{ordem.lower()}s/{tamanho}{ordem}{tipo}.txt"
                vetor = []

                leituraArquivo(vetor, nomeArquivo)

                tempoMedio = 0.0
                for _ in range(10):
                    vetorCopia = vetor[:]
                    inicio = datetime.utcnow()
                    radixSort(vetorCopia)
                    fim = datetime.utcnow()
                    tempo = (fim - inicio).total_seconds()
                    tempoTotal += tempo
                    tempoMedio += tempo

                media = tempoMedio / 10.0
                tabelaSaida += (f"{media:.8},")

        tabelaSaida += ("\n")

    tabelaSaida += (f"Tempo Total,{tempoTotal:.10}\n")
    tabelaSaida += (f"Tempo Médio Total,{tempoTotal / 720:.8}\n")
    return tabelaSaida

def radixSort(vetor):
    def achaMaior(vetor):
        maior = 0
        for i in vetor:
            if i > maior:
                maior = i
        return maior

    def countingSort(vetor, exp):
        saida = [0] * len(vetor)
        count = [0] * 10

        for i in vetor:
            count[(i // exp) % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = len(vetor) - 1
        while i >= 0:
            saida[count[(vetor[i] // exp) % 10] - 1] = vetor[i]
            count[(vetor[i] // exp) % 10] -= 1
            i -= 1

        for i in range(len(vetor)):
            vetor[i] = saida[i]

    maior = achaMaior(vetor)
    exp = 1

    while maior // exp > 0:
        countingSort(vetor, exp)
        exp *= 10
