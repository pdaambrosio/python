[n1, n2, n3, n4] = map(float, input().split())

average = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10

if average >= 7:
    print('Media: {:.1f}\nAluno aprovado.'.format(average))
elif average < 5:
    print('Media: {:.1f}\nAluno reprovado.'.format(average))
else:
    exam = float(input())
    final_grade = (average + exam) / 2
    result = ['Aluno aprovado.' if final_grade >= 5 else 'Aluno reprovado.']
    print('Media: {:.1f}\nAluno em exame.\nNota do exame: {:.1f}'.format(average, exam))
    print('{[0]} \nMedia final: {:.1f}'.format(result, final_grade))
