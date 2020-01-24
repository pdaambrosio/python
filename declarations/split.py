# Use for, split() e if para criar uma declaração que imprima as palavras que começam com 's':

st = 'Print only the words that start with s in this sentence'

for word in st.split():
    if word[0] == 's':
        print(word)
