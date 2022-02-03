def searching_subsequences(seq1: str, seq2: str) -> str:
    amount: int = seq2.count(seq1)
    
    if amount == 0:
        return 'Nao existe subsequencia\n'
    else:
        position: int = seq2.rfind(seq1)
        return f'Qtd.Subsequencias: {amount}\nPos: {position + 1}\n'
        

def main():
    case: int = 1
    while True:
        try:
            N1 = input()
            N2 = input()
            print(f'Caso #{case}:')
            print(searching_subsequences(N1, N2))
        except EOFError:
            break
        
        case += 1


main()
