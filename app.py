import re

def processamento_texto(textos):
    textos = textos.lower()
    textos = re.sub(r'[^a-zà-ú\s]', '', textos)
    palavras = textos.split()
    return palavras

if __name__ == "__main__":
    palavras_biblia = processamento_texto()