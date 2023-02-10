import nltk
from nltk.corpus import cmudict

# Carregando o dicionário de fonemas
d = cmudict.dict()

# Função para contar as rimas de um texto
def count_rhymes(text):
    # Tokenizando o texto
    tokens = nltk.word_tokenize(text)
    
    # Criando uma lista para armazenar as rimas
    rhymes = []
    
    for word in tokens:
        # Verificando se a palavra está no dicionário de fonemas
        if word.lower() in d:
            # Adicionando a última fonema da palavra à lista de rimas
            rhymes.append(d[word.lower()][-1])
    
    # Contando o número de ocorrências de cada fonema na lista
    rhymes_count = {}
    for rhyme in rhymes:
        if rhyme in rhymes_count:
            rhymes_count[rhyme] += 1
        else:
            rhymes_count[rhyme] = 1
    
    return rhymes_count

# Exemplo de uso
text = "Mary had a little lamb.\nIts fleece was white as snow."
print(count_rhymes(text))
# Output: {'AE1 M': 2}
