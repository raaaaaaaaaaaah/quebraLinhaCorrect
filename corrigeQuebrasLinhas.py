import csv

def corrigir_quebras_csv(entrada, saida, delimitador=";"):
    
    #Lê um CSV com possíveis quebras de linha dentro de campos e grava um novo arquivo corrigido.
    
    
    with open(entrada, "r", encoding="utf-8", newline="") as f_entrada, \
         open(saida, "w", encoding="utf-8", newline="") as f_saida:

        leitor = csv.reader(f_entrada, delimiter=delimitador, quotechar='"')
        escritor = csv.writer(f_saida, delimiter=delimitador, quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for linha in leitor:
            escritor.writerow(linha)

    print(f"[OK] Arquivo corrigido salvo como: {saida}")


# Exemplo de uso:
corrigir_quebras_csv("dados_bagunçados.csv", "dados_corrigidos.csv")
