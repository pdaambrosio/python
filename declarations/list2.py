# Use Compreensão em listas para criar uma lista das primeiras letras de cada palavra na string abaixo:

st='Create a list of the first letters of every word in this string'

l=[word[0] for word in st.split()]

print(l)
