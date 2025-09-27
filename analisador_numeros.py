import matplotlib.pyplot as plt

def analisar_numeros(numeros):
    soma = sum(numeros)
    media = soma / len(numeros)
    maior = max(numeros)
    menor = min(numeros)

    return {
        "quantidade": len(numeros),
        "soma": soma,
        "media": media,
        "maior": maior,
        "menor": menor
    }

def salvar_resultados(resultados, arquivo="resultados.txt"):
    with open(arquivo, "w") as f:
        for chave, valor in resultados.items():
            f.write(f"{chave}: {valor}\n")

def gerar_grafico(numeros):
    plt.bar(range(len(numeros)), numeros)
    plt.title("Distribuição dos Números")
    plt.xlabel("Índice")
    plt.ylabel("Valor")
    plt.savefig("grafico.png")
    plt.show()

if __name__ == "__main__":
    print("=== ANALISADOR DE NÚMEROS ===")
    entrada = input("Digite números separados por espaço: ")
    numeros = [float(n) for n in entrada.split()]

    resultados = analisar_numeros(numeros)
    
    print("\n📊 Resultados da Análise:")
    for k, v in resultados.items():
        print(f"{k}: {v}")

    salvar = input("\nDeseja salvar os resultados em arquivo? (s/n): ").lower()
    if salvar == "s":
        salvar_resultados(resultados)
        print("✅ Resultados salvos em resultados.txt")

    grafico = input("Deseja gerar gráfico? (s/n): ").lower()
    if grafico == "s":
        gerar_grafico(numeros)
