def palindrome(s):
    
    s = s.replace(' ','') # Isso substitui todos os espaços "" sem espaço ". (Soluciona problemas com strings que têm espaços)
    return s == s[::-1]
