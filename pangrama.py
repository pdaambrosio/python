'''
Escreva uma função Python para verificar se uma string é um pangrama ou não.
Nota: Pangramas são palavras ou frases contendo cada letra do alfabeto pelo menos uma vez.
Dica: veja o módulo de strings
'''
import string

def pangram(str1, alphabet=string.ascii_lowercase):
    alphaset=set(alphabet)
    print (alphaset <= set(str1.lower()))
 
pangram('The quick brown fox jumps over the lazy dog')




