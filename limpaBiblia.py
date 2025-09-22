import re

def limpar_biblia(caminho_entrada = 'biblia.txt', caminho_saida = 'biblia_limpa.txt'):
    with open(caminho_entrada, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    linhas_limpa = []
    for linha in linhas:
        linha = linha.strip()

        if not linha:
            continue
        if re.fullmatch(r'[A-ZÁÉÍÓÚÂÊÔÃÕÇ ]+', linha):
            continue  # Ignora Livro e marcações
        if re.fullmatch(r'[A-ZÁÉÍÓÚÂÊÔÃÕÇ ]+\s+\d+', linha):
            continue  # Ignora Capítulo
        linha = re.sub(r'^\d+\s+', '', linha)  # Remove número do versículo
        linhas_limpa.append(linha)

    with open(caminho_saida, 'w', encoding='utf-8') as f:
        f.write("\n".join(linhas_limpa))

if __name__ == "__main__":
    entrada = 'biblia.txt'
    saida = 'biblia_limpa.txt'
    limpar_biblia(entrada, saida)
    print(f"{entrada} limpa e salva em: {saida}")
