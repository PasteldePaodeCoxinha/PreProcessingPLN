import nltk
import re

def tokeninzar_sentenca(texto):
    sentencas = nltk.sent_tokenize(texto)
    return sentencas

def processamento_texto(textos):
    textos = textos.lower()
    textos = re.sub(r'[^a-zà-ú\s]', '', textos)
    palavras = textos.split()
    return palavras

if __name__ == "__main__":
    with open("biblia_limpa.txt", "r", encoding="utf-8") as f:
        biblia_textos = f.read()

    sentencas_biblia = tokeninzar_sentenca(biblia_textos)

    sentencas_biblias_tokenizadas = []

    for frase in sentencas_biblia[:40]:
        sentencas_biblias_tokenizadas.append(processamento_texto(frase))
    
    print(sentencas_biblias_tokenizadas)