from radixSort import calcularTabelaSaidaRadix
from arquivos import escritaArquivo

def main():
    nomeArquivoSaida = "datasets/tempoExecucao-Python"
    tabelaSaida = ""

    print("Calculando tabela de saída do Radix Sort...")
    tabelaSaida = calcularTabelaSaidaRadix([10000, 100000, 500000, 1000000], tabelaSaida)
    escritaArquivo(nomeArquivoSaida, tabelaSaida)
    print("Tabela de saída do Radix Sort calculada com sucesso!")

main()