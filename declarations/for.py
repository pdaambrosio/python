# Percorra a string abaixo e se o comprimento de uma palavra for par imprima "é par!"

st='Print every word in this sentence that has an even number of letters'
split_string=st.split()

for word in st.split():
   if len(word) %2 == 0:
     print (word+': é par')
