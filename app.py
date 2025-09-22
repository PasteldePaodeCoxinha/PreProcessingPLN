import re

def processamento_texto(textos):
    textos = textos.lower()
    textos = re.sub(r'[^a-zà-ú\s]', '', textos)
    palavras = textos.split()
    return palavras

if __name__ == "__main__":
    with open("biblia_limpa.txt", "r", encoding="utf-8") as f:
        biblia_textos = f.read()

    palavras_biblia = processamento_texto(biblia_textos)